import flask
import pymysql.cursors


def get_application(user_id):
    """
    Returns the application information for a given user_id
    as a dictionary
    Also returns the diet and demographics portion as a list 
    within the dict
    """
    result = []
    query = """
    SELECT user_id, first_name, preferred_name, middle_name, last_name,
    phone, school, major, degree_type, graduation_year, 
    github, linkedin, resume, latino, gender, shirt_size, 
    transportation, in_state, bus_from, airport, 
    diet_rest, diet_rest_detail, 
    q1, q2, q3, q4, code_of_conduct 
    FROM users NATURAL JOIN members NATURAL JOIN 
    applications NATURAL JOIN status WHERE user_id = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        result = cursor.fetchone()

    if result is None:
        return None

    query = """
    SELECT race_type FROM race WHERE user_id = %s
    """

    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        race_info_dict = cursor.fetchall()
    race_info = [x['race_type'] for x in race_info_dict]
    result['race'] = race_info
    print(result['resume'])
    result['resume_url'] = generate_resume_url("Ziyan_Mo_resume_5.0.4.pdf")
    print(result)
    return result

def generate_resume_url(resume_name):
    return flask.url_for("judging.uploaded_file", filename=resume_name) 

def get_all_application_links():
    """
    Returns a list which contains a dictionary. 
    This dictionary contains the name, user_id, status, and link
    to their view applications page. 
    """
    result = []
    query = """
    SELECT user_id, first_name, last_name, status 
    FROM members NATURAL JOIN status
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [])
        result = cursor.fetchall()
    print(result)
    for i in result:
        i['link'] = flask.url_for(
            "judging.view_application", user_id=i['user_id'], _external=True)
    return result


def update_status(user_id, new_status):
    """
    Given a user_id and a status, update the status in the status
    table. 
    """
    query = """
    UPDATE status SET status = %s WHERE user_id = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [new_status, user_id])
