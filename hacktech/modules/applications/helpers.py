import flask
from hacktech import auth_utils
from hacktech import app_year
import hacktech.modules.judging.helpers as judging_helpers
from werkzeug.utils import secure_filename
import os

SCHOOLS = []


def get_schools():
    schools = []
    global SCHOOLS
    if SCHOOLS != []:
        return SCHOOLS
    # Cache this.
    with open(
            "/home/hacktech/hacktechpy.io/hacktech/modules/applications/schools.txt"
    ) as f:
        for line in f:
            line = line.rstrip()
            if line != "":
                schools.append(line.rstrip())
    SCHOOLS = schools
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
    return "Accepted" == status['status'] or "Declined" == status['status'] \
            or "RSVPed" == status['status']


def check_submitted(self_email, other_email):
    status = check_status(self_email, other_email)
    return "Submitted" == status['status'] or "Accepted" == status['status'] \
            or "Declined" == status['status'] or "RSVPed" == status['status'] \
            or "Rejected" == status['status']


ALLOWED_EXTENSIONS = set(['pdf'])

# 5 MB
MAX_FILE_SIZE = 5000 * 1024


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
    ) in ALLOWED_EXTENSIONS and file_length > 0 and file_length < MAX_FILE_SIZE


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
def update_status(email, status, reimbursement_amount):
    user_id = get_user_id(email)

    query = """
    UPDATE status SET status = %s WHERE user_id = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [status, user_id])
    return


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
    def __init__(self, application, member, diet, race):
        self.first_name = member['first_name'] or ''
        self.middle_name = member['middle_name'] or ''
        self.last_name = member['last_name'] or ''
        self.preferred_name = member['preferred_name'] or ''
        self.phone = application['phone'] or ''
        self.school = application['school'] or ''
        self.major = application['major'] or ''
        self.degree_type = application['degree_type'] or ''
        self.graduation_year = application['graduation_year'] or ''
        self.github = application['github'] or ''
        self.linkedin = application['linkedin'] or ''
        self.resume = application['resume'] or ''
        if application['latino'] is None:
            self.latino = ''
        else:
            self.latino = application['latino']
        self.gender = application['gender'] or ''
        self.shirt_size = application['shirt_size'] or ''
        self.transportation = application['transportation']
        self.in_state = application['in_state']
        self.bus_from = application['bus_from'] or ''
        self.airport = application['airport'] or ''
        self.diet_rest = application['diet_rest']
        self.diet_rest_detail = application['diet_rest_detail'] or ''
        self.q1 = application['q1'] or ''
        self.q2 = application['q2'] or ''
        self.q3 = application['q3'] or ''
        self.q4 = application['q4'] or ''
        self.q5 = application['q5'] or ''
        self.q6 = application['q6'] or ''
        self.code_of_conduct = application['code_of_conduct']
        self.diet_types = [entry['diet_restrictions'] for entry in diet]
        self.race_types = [entry['race_type'] for entry in race]
        self.resume_link = judging_helpers.generate_resume_url(self.resume)
        self.resume_original_name = ""
        self.major_opt = ""
        self.school_opt = ""
        if self.resume is not None and self.resume != "":
            self.resume_original_name = "_".join(
                self.resume.split("_")[:-1]) + ".pdf"


class ValidationForm:
    def __init__(self):
        self.info = {}
        self.info["first_name"] = ""
        self.info["last_name"] = ""
        self.info["phone"] = ""
        self.info["school"] = ""
        self.info["degree_type"] = ""
        self.info["graduation_year"] = ""
        self.info["resume"] = ""
        self.info["gender"] = ""
        self.info["shirt_size"] = ""
        self.info["transportation"] = ""
        self.info["diet_rest"] = ""
        self.info["q1"] = ""
        self.info["q2"] = ""
        self.info["q3"] = ""
        self.info["q4"] = ""
        self.info["q5"] = ""
        self.info["q6"] = ""
        self.info["code_of_conduct"] = ""

    def fill(self, application, member):
        self.info[
            "first_name"] = "" if member['first_name'] != "" else "has-error"
        self.info[
            "last_name"] = "" if member['last_name'] != "" else "has-error"
        self.info["phone"] = "" if application['phone'] != "" else "has-error"
        self.info[
            "school"] = "" if application['school'] != "" and application['school'] != "N/A" else "has-error"
        self.info[
            "degree_type"] = "" if application['degree_type'] != "" else "has-error"
        self.info[
            "graduation_year"] = "" if application['graduation_year'] != "" else "has-error"
        self.info[
            "resume"] = "" if application['resume'] != None and application['resume'] != "" else "has-error"
        self.info[
            "gender"] = "" if application['gender'] != "" else "has-error"
        self.info[
            "shirt_size"] = "" if application['shirt_size'] != "" else "has-error"
        self.info[
            "transportation"] = "" if application['transportation'] != None else "has-error"
        self.info[
            "diet_rest"] = "" if application['diet_rest'] != None else "has-error"
        self.info["q1"] = "" if application['q1'] != "" else "has-error"
        self.info["q2"] = "" if application['q2'] != "" else "has-error"
        self.info["q3"] = "" if application['q3'] != "" else "has-error"
        self.info["q4"] = "" if application['q4'] != "" else "has-error"
        self.info["q5"] = "" if application['q5'] != "" else "has-error"
        self.info["q6"] = "" if application['q6'] != "" else "has-error"
        self.info["code_of_conduct"] = ""  # if application[
        # 'code_of_conduct'] == 1 else "has-error"


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
        application = cursor.fetchone()
    query = """
    SELECT * FROM members WHERE user_id = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        member = cursor.fetchone()
    query = """
    SELECT * FROM diet WHERE user_id = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        diet = cursor.fetchall()
    query = """
    SELECT * FROM race WHERE user_id = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        race = cursor.fetchall()
    validationForm = ValidationForm()
    validationForm.fill(application, member)
    return (FormInfo(application, member, diet, race), validationForm)


def handle_update_applications(
        action, email, phone_number, school, major, degree_type,
        graduation_year, github, linkedin, resume_file, latino, race, gender,
        shirt_size, need_transportation, bus_from, airport,
        dietary_restrictions, diet_choices, diet_details, q1, q2, q3, q4, q5, q6,
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
    validations = ValidationForm()
    flask.g.pymysql_db.begin()
    try:
        # Insert the new row into applications, or update if it exists.
        query = """
        INSERT INTO applications (user_id, application_year, phone, school, 
        major, degree_type, graduation_year, github, linkedin, resume, latino,
        gender, shirt_size, transportation, in_state, bus_from, airport, 
        diet_rest, diet_rest_detail, q1, q2, q3, q4, q5, q6, code_of_conduct)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
        q5 = VALUES(q5),
        q6 = VALUES(q6),
        code_of_conduct = VALUES(code_of_conduct)
        """

        latino_bool = None
        if latino == "True":
            latino_bool = True
        elif latino == "False":
            latino_bool = False

        in_state = None
        if need_transportation == "insideCA" or need_transportation == "no":
            in_state = True
        elif need_transportation == "outsideCA":
            in_state = False

        transportation = None
        if need_transportation == "insideCA" or need_transportation == "outsideCA":
            transportation = True
        elif need_transportation == "no":
            transportation = False

        diet_rest = None
        if dietary_restrictions == "True":
            diet_rest = True
        elif dietary_restrictions == "False":
            diet_rest = False
        resume_name = ""
        last_resume_name = check_resume_exists(get_user_id(email))
        if resume_file and allowed_file(resume_file):
            resume_name = secure_filename(resume_file.filename)
            resumes_root_path = os.path.join(
                flask.current_app.root_path,
                flask.current_app.config['RESUMES'])
            resume_name = resume_name.split(".")
            resume_name = secure_filename(
                str(resume_name[:-1]) + '_' + str(get_user_id(email)) + ".pdf")

            resume_file.save(os.path.join(resumes_root_path, resume_name))
        if resume_name == "":
            resume_name = last_resume_name

        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [
                user_id, app_year.year + "0000", phone_number, school, major,
                degree_type, graduation_year, github, linkedin, resume_name,
                latino_bool, gender, shirt_size, transportation, in_state,
                bus_from, airport, diet_rest, diet_details, q1, q2, q3, q4, q5, q6,
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
        fields = [
            first_name, last_name, phone_number, school, degree_type,
            graduation_year, shirt_size, q1, q2, q3, q4, q5, q6,
        ]
        # removed need_transportation, dietary_restrictions, code_of_conduct
        for field in fields:
            if not field:
                return (False, "Please fill out the required fields in red.")

        if (resume_file is None
                or resume_file.filename == '') and not last_resume_name:
            return (False, "Please upload your resume.")
        if (resume_file and
                resume_file.filename != "") and not allowed_file(resume_file):
            return (
                False,
                'Please upload your resume as a PDF file less than 500 KB.')
        else:
            update_status(email, "Submitted", None)
        return (True, "You have submitted your application successfully!")
    update_status(email, "In-Progress", None)
    return (True, "Your application has been updated!")


def check_resume_exists(user_id):
    query = """
    SELECT resume FROM applications WHERE user_id = %s AND
    application_year = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id, app_year.year + "0000"])
        res = cursor.fetchone()
    return None if res == None or res['resume'] == "" else res['resume']
