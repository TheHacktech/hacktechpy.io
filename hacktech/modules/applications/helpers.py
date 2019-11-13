import flask
from hacktech import auth_utils


def check_accepted(self_email, other_email):
    return "Accepted" == check_status(self_email, other_email)


### TODO!
def check_status(self_email, other_email):
    """
    Using the user's email, check the user's status for the
    current year and return it.
    """
    # If they aren't an admin or thye aren't themselves,
    # then they shouldn't see status
    if not auth_utils.check_admin(self_email) and self_email != other_email:
        return ""
    query = """
    SELECT status FROM users NATURAL JOIN status WHERE
    email = %s
    """

    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [other_email])
        result = cursor.fetchone()
    return result['status']


def handle_update_applications(
        email, phone_number, school, major, degree_type, graduation_year,
        github, linkedin, resume, latino, race, gender, shirt_size,
        need_transportation, bus_from, airport, dietary_restrictions,
        diet_choices, diet_details, q1, q2, q3, q4, code_of_conduct):
    """Handles application updates by updating the applications table in 
    the database with application form info."""
    query = "SELECT user_id FROM users WHERE email = %s"
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, email)
        result = cursor.fetchone()
    user_id = result['user_id']
    if not user_id:
        return (False, "Invalid user ID. Please contact the organizers.")
    # TODO: save function, check for existing application by user id
    flask.g.pymysql_db.begin()
    try:
        # Insert the new row into applications.
        query = """
        INSERT INTO applications (user_id, application_year, phone, school, 
        major, degree_type, graduation_year, github, linkedin, resume, latino,
        gender, shirt_size, transportation, in_state, bus_from, airport, 
        diet_rest, diet_rest_detail, q1, q2, q3, q4, code_of_conduct)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s )
        """
        latino = (latino != "False")
        in_state = (need_transportation != "outsideCA")
        transportation = (need_transportation != "no")
        diet_rest = (dietary_restrictions != "True")
        code_of_conduct = (code_of_conduct != "False")
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [
                user_id, "2020", phone_number, school, major, degree_type,
                graduation_year, github, linkedin, resume, latino, gender,
                shirt_size, transportation, in_state, bus_from, airport,
                diet_rest, diet_details, q1, q2, q3, q4, code_of_conduct
            ])
        # Insert new row into diet table for each dietary restriction choice.
        query = """
        INSERT INTO diet (user_id, diet_restrictions)
        VALUES(%s, %s)
        """
        for diet in diet_choices:
            with flask.g.pymysql_db.cursor() as cursor:
                cursor.execute(query, [user_id, diet])
        # Insert new row into race table for each race type.
        query = """
        INSERT INTO race (user_id, race_type)
        VALUES(%s, %s)
        """
        for race_type in race:
            with flask.g.pymysql_db.cursor() as cursor:
                cursor.execute(query, [user_id, race_type])
        flask.g.pymysql_db.commit()
    except Exception as e:
        print(e)
        flask.g.pymysql_db.rollback()
        return (False,
                "An unexpected error occurred. Please contact the organizers.")
    return (True, "")
