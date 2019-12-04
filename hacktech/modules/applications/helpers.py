import flask
from hacktech import auth_utils
from hacktech import app_year
import hacktech.modules.judging.helpers as judging_helpers
import os

def get_schools():
    schools = []
    with open("/home/hacktech/hacktechpy.io/hacktech/modules/applications/schools.txt") as f:
        for line in f:
            schools.append(line.rstrip())
    return schools


def get_majors():
    majors = [
        "Astronomy", "Bioengineering", "Biology", "Chemical Engineering",
        "Chemistry", "Computer Engineering", "Computer Science",
        "Electrical Engineering", "Mathematics", "Mechanical Engineering",
        "N/A", "Physics"
    ]
    return majors


def check_accepted(self_email, other_email):
    status = check_status(self_email, other_email)
    return "Accepted" == status['status'] or "Declined" == status['status'] or "RSVPed" == status['status']


ALLOWED_EXTENSIONS = set(['pdf'])

# 500 KB
MAX_FILE_SIZE = 500 * 1024


def allowed_file(file):
    '''
    Checks for allowed file extensions.
    '''
    splits = file.filename.rsplit('.', 1)
    file.seek(0, os.SEEK_END)
    file_length = file.tell()
    # Reset to beginning of file
    file.seek(0, 0)
    return len(splits) >= 2 and splits[1].lower(
    ) in ALLOWED_EXTENSIONS and file_length < MAX_FILE_SIZE


def check_status(self_email, other_email):
    """
    Using the user's email, check the user's status for the
    current year and return it.
    """
    # If they aren't an admin or they aren't themselves,
    # then they shouldn't see status
    if not auth_utils.check_admin(self_email) and self_email != other_email:
        return ""
    query = """
    SELECT status, reimbursement_amt FROM users NATURAL JOIN status NATURAL JOIN applications WHERE
    email = %s AND application_year = %s
    """

    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [other_email, app_year.year + "0000"])
        result = cursor.fetchone()
    if result == None:
        return None
    return result


### TODO: Move these into a utils/helpers/core file.
def update_status(email, status):
    user_id = get_user_id(email)
    judging_helpers.update_status(user_id, status)


def get_user_id(email):
    query = """
    SELECT user_id FROM users WHERE
    email = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [email])
        result = cursor.fetchone()
    if 'user_id' not in result:
        return None
    return result['user_id']

class FormInfo:
    def __init__(self, application):
        self.phone = application['phone']
        self.school = application['school']
        self.major = application['major']
        self.degree_type = application['degree_type']
        self.graduation_year = application['graduation_year']
        self.github = application['github']
        self.linkedin = application['linkedin']
        self.resume = application['resume']
        self.latino = application['latino']
        self.gender = application['gender']
        self.shirt_size = application['shirt_size']
        self.transportation = application['transportation']
        self.in_state = application['in_state']
        self.bus_from = application['bus_from']
        self.airport = application['airport']
        self.diet_rest = application['diet_rest']
        self.diet_rest_detail = application['diet_rest_detail']
        self.q1 = application['q1']
        self.q2 = application['q2']
        self.q3 = application['q3']
        self.q4 = application['q4']
        self.code_of_conduct = application['code_of_conduct']

def get_form_info(email):
    """Gets all existing application form info from the database."""
    user_id = get_user_id(email)
    if not user_id:
        return (False, "Invalid user ID. Please contact the organizers.")
    query = """
    SELECT * FROM applications WHERE user_id = %s AND application_year = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id, app_year.year + "0000"])
        result = cursor.fetchone()
    return FormInfo(result)

def handle_update_applications(
        action, email, phone_number, school, major, degree_type,
        graduation_year, github, linkedin, resume, latino, race, gender,
        shirt_size, need_transportation, bus_from, airport,
        dietary_restrictions, diet_choices, diet_details, q1, q2, q3, q4,
        code_of_conduct, first_name, middle_name, last_name, preferred_name):
    """Handles application updates by updating the applications table in 
    the database with application form info, updating status table if 
    application is submitted."""
    query = "SELECT user_id FROM users WHERE email = %s"
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, email)
        result = cursor.fetchone()
    user_id = result['user_id']
    if not user_id:
        return (False, "Invalid user ID. Please contact the organizers.")
    flask.g.pymysql_db.begin()
    try:
        # Insert the new row into applications, or update if it exists.
        query = """
        INSERT INTO applications (user_id, application_year, phone, school, 
        major, degree_type, graduation_year, github, linkedin, resume, latino,
        gender, shirt_size, transportation, in_state, bus_from, airport, 
        diet_rest, diet_rest_detail, q1, q2, q3, q4, code_of_conduct)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s )
        ON DUPLICATE KEY UPDATE
        phone = VALUES(phone),
        school = VALUES(school),
        major = VALUES(major),
        degree_type = VALUES(degree_type),
        graduation_year = VALUES(graduation_year),
        github = VALUES(github),
        linkedin = VALUES(linkedin),
        resume = VALUES(resume),
        latino = VALUES(latino),
        gender = VALUES(gender),
        shirt_size = VALUES(shirt_size),
        transportation = VALUES(transportation),
        in_state = VALUES(in_state),
        bus_from = VALUES(bus_from),
        airport = VALUES(airport),
        diet_rest = VALUES(diet_rest),
        diet_rest_detail = VALUES(diet_rest_detail),
        q1 = VALUES(q1),
        q2 = VALUES(q2),
        q3 = VALUES(q3),
        q4 = VALUES(q4),
        code_of_conduct = VALUES(code_of_conduct)
        """
        latino = (latino == "True")
        in_state = (need_transportation == "insideCA"
                    or need_transportation == "no")
        transportation = (need_transportation == "insideCA"
                          or need_transportation == "outsideCA")
        diet_rest = (dietary_restrictions == "True")
        code_of_conduct = (code_of_conduct == "True")
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [
                user_id, app_year.year + "0000", phone_number, school, major,
                degree_type, graduation_year, github, linkedin, resume, latino,
                gender, shirt_size, transportation, in_state, bus_from,
                airport, diet_rest, diet_details, q1, q2, q3, q4,
                code_of_conduct
            ])
        # Update members table with name info from application.
        query = """
        UPDATE members
        SET first_name=%s, middle_name=%s, last_name=%s, preferred_name=%s
        WHERE user_id=%s 
        """
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [
                first_name, middle_name, last_name, preferred_name, user_id
            ])
        # Delete existing rows in diet table for this user.
        query = """
        DELETE FROM diet
        WHERE user_id = %s
        """
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [user_id])
        # Insert new row into diet table for each dietary restriction choice.
        query = """
        INSERT INTO diet (user_id, diet_restrictions)
        VALUES(%s, %s)
        """
        for diet in diet_choices:
            with flask.g.pymysql_db.cursor() as cursor:
                cursor.execute(query, [user_id, diet])
        # Delete existing rows in race table for this user.
        query = """
        DELETE FROM race
        WHERE user_id = %s
        """
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [user_id])
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
    # Check all required fields are filled out
    if action == 'Submit':
        if not school or not degree_type or not graduation_year or not shirt_size \
                or not need_transportation or dietary_restrictions == "" \
                or not q1 or not q2 or not q3 or not q4 or not first_name \
                or not last_name:
            return (False,
                    "Please fill out all required fields before submitting.")
        if not code_of_conduct:
            return (
                False,
                "You must accept the MLH code of conduct and data sharing provision."
            )
        else:
            # Update status
            pass
    return (True, "")
