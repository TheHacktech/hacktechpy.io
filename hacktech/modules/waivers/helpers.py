import flask
from hacktech import auth_utils
from hacktech import app_year
import hacktech.modules.judging.helpers as judging_helpers
from hacktech.modules.applications.helpers import allowed_file
from werkzeug.utils import secure_filename
import os
import PyPDF2


def get_waiver_status(user_id, waiver_type):
    query = """
    SELECT {0}_status FROM {0} where user_id = %s""".format(waiver_type)
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, user_id)
        res = cursor.fetchone()
    key = "{0}_status".format(waiver_type)
    return "Not Submitted" if res == None else res[key]


def get_full_name(uid):
    query = "SELECT first_name, last_name FROM members WHERE user_id = %s"
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, uid)
        res = cursor.fetchone()
    if res is None:
        return ("", "")
    return (res['first_name'], res['last_name'])


def save_info(email, waiver_file, app_folder, waiver_type):
    uid = auth_utils.get_user_id(email)
    first_name, last_name = get_full_name(uid)
    waiver_file_name = last_name + "_" + first_name + "_" + str(uid) + ".pdf"
    waiver_root_path = os.path.join(flask.current_app.root_path,
                                    flask.current_app.config[app_folder])
    waiver_path = os.path.join(waiver_root_path, waiver_file_name)
    print(waiver_file, allowed_file(waiver_file))
    if waiver_file and allowed_file(waiver_file):
        if os.path.exists(waiver_path):
            os.remove(waiver_path)
        waiver_file.save(waiver_path)
        query = "INSERT INTO {0}(user_id, {0}_path, {0}_status, submitted_time) VALUES (%s, %s, 'Submitted', NOW()) ON DUPLICATE KEY UPDATE {0}_status =  'Submitted', submitted_time = NOW()".format(
            waiver_type)

        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [uid, waiver_file_name])
        return waiver_path
    return ""
