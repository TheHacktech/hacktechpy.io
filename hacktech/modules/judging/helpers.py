import flask
import pymysql.cursors
from hacktech import app_year

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
    for i in result:
        i['link'] = flask.url_for(
            "judging.view_application", user_id=i['user_id'], _external=True)
    return result

def get_current_stats():
    stats = {}
    query = """
    SELECT status, COUNT(*) FROM status NATURAL JOIN 
    applications WHERE application_year = %s
    GROUP BY status
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [app_year.year])
        res = cursor.fetchall()
    cats = ["shirt_size", "school", "major", "degree_type", "graduation_year", "in_state", "bus_from"]
    ### TODO: SELECT ONLY THE CURRENT YEAR!!!!
    for cat in cats:
        query = """
        SELECT {0}, COUNT(*) from applications 
        GROUP BY {0}
        """.format(cat)
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query)#, [app_year.year])
            res = cursor.fetchall()
        print(res)
        stats[cat] = reorder_stat(res, cat)
    return stats

def reorder_stat(res, col_name):
    labels = []
    data = []
    for i in res:
        labels.append(str(i[col_name]))
        data.append(i['COUNT(*)'])
    return {"labels":labels, "data":data}

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
