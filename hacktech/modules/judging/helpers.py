import flask
import pymysql.cursors


def get_application(user_id):
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
    return result


def get_all_application_links():
    result = []
    query = """
    SELECT user_id, first_name, last_name, status 
    FROM members NATURAL JOIN status
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [])
        result = cursor.fetchall()
    for i in result:
        i['link'] = flask.url_for(
            "judging.view_application", user_id=i['user_id'], _external=True)
    return result


def update_status(user_id, new_status):
    query = """
    UPDATE status SET status = %s WHERE user_id = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [new_status, user_id])
