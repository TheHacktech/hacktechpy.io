import flask
from hacktech import auth_utils
from hacktech import app_year
import hacktech.modules.judging.helpers as judging_helpers
from hacktech.modules.applications.helpers import allowed_file
from werkzeug.utils import secure_filename
import os
import PyPDF2


def submitted_caltech_waiver(email):
    query = """
    SELECT waiver_status FROM caltech_waiver where user_id = %s"""
    
    pass


def submitted_medical_info(email):
    pass


def get_full_name(uid):
    query = "SELECT first_name, last_name FROM members WHERE user_id = %s"
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, uid)
        res = cursor.fetchone()
    if res is None:
        return ("", "")
    return (res['first_name'], res['last_name'])

def save_info(email, waiver_file, app_folder, table_name):
    uid = auth_utils.get_user_id(email)
    first_name, last_name = get_full_name(uid)
    waiver_file_name = last_name+"_"+first_name + "_" + str(uid)+".pdf"
    waiver_root_path = os.path.join(
            flask.current_app.root_path,
            flask.current_app.config[app_folder])
    waiver_path = os.path.join(waiver_root_path, waiver_file_name)

    if waiver_file and allowed_file(waiver_file):
        waiver_file.save(waiver_path)
        query = "INSERT INTO "+table_name+"(user_id, waiver_path, waiver_status, submitted_time) VALUES (%s, %s, 'Submitted', NOW())"
        
        with flask.g.pymysql_db.cursor() as cursor:
             cursor.execute(query, [uid, waiver_file_name])
        return waiver_path 
    return ""

