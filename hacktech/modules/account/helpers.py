import flask

from hacktech import auth_utils
from hacktech import email_templates
from hacktech import email_utils
from hacktech import misc_utils
from hacktech import validation_utils
from hacktech import app_year


def get_user_data(user_id):
    """Returns user data for the create account form."""
    query = """
    SELECT email,
    FROM users
    WHERE user_id = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        return cursor.fetchone()


def handle_create_account(email, password, password2, first_name, middle_name,
                          preferred_name, last_name, dob):
    query = """
    SELECT email
    FROM users
    WHERE email = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [email])
        result = cursor.fetchone()
    if result is not None:
        return (False, "You already have an account. Try recovering it?")

    if not validation_utils.validate_password(password, password2):
        return (False, "Make sure your passwords match!")
    flask.g.pymysql_db.begin()
    try:
        confirm_account_key = auth_utils.generate_confirm_account_key()
        # Insert the new row into users.
        query = """
        INSERT INTO users (email, password_hash, confirm_account_key)
        VALUES (%s, %s, %s)
        """
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [email, "", confirm_account_key])
        # Set the password.
        auth_utils.set_password(email, password)

        query = """
        SELECT user_id FROM users WHERE email = %s
        """
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [email])
            result = cursor.fetchone()
        user_id = result["user_id"]

        # Set rest of the info...
        query = """
        INSERT INTO members (user_id, first_name, preferred_name, middle_name, 
        last_name, date_of_birth)
        VALUES(%s, %s, %s, %s, %s, %s)
        """
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [
                user_id, first_name, preferred_name, middle_name, last_name,
                dob
            ])
        query = """
        INSERT INTO applications (user_id, application_year) 
        VALUES(%s, %s)
        """
        ## TODO: Make sure to select it only from the current application year
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [user_id, app_year.year + "0000"])
        query = """ 
        SELECT application_id FROM applications 
        WHERE user_id = %s
        """
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [user_id])
            application_id = cursor.fetchone()
            application_id = application_id['application_id']

        query = """
        INSERT INTO status (user_id, application_id, status) 
        VALUES(%s, %s, %s)
        """
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [user_id, application_id, 'Not Started'])

        flask.g.pymysql_db.commit()
        subject = "Thanks for creating an account!"
        msg = email_templates.CreateAccountSuccessfulEmail.format(first_name)
        email_utils.send_email(email, msg, subject)
    except Exception as e:
        print(e)
        flask.g.pymysql_db.rollback()
        return (
            False,
            "An unexpected error occurred. Please contact the hacktech organizers"
        )
    return (True, "")
