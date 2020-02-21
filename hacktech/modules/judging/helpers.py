import flask
import pymysql.cursors
from datetime import date
from hacktech import app_year
from hacktech import email_templates, email_utils
from PyPDF2 import PdfFileMerger
import os
from hacktech import auth_utils

def generate_resume_book(fields):
    query = """
    SELECT resume FROM users NATURAL JOIN status NATURAL JOIN applications WHERE
    status = %s AND application_year = %s
    """
    resume_names = []
    upload_folder = os.path.join(flask.current_app.root_path,
                                 flask.current_app.config['RESUMES'])
    for i in fields:
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [i, app_year.year + "0000"])
            res = cursor.fetchall()
            resume_names.extend([
                os.path.join(upload_folder, i['resume']) for i in res
                if i['resume'] is not None and i['resume'] != ""
            ])
    collect(resume_names)


def collect(resume_names):
    upload_folder = os.path.join(flask.current_app.root_path,
                                 flask.current_app.config['RESUMES'])
    resume_book_path = os.path.join(upload_folder, "hacktech_resume_book.pdf")
    merger = PdfFileMerger()
    for resumes in resume_names:
        print(resumes)
        merger.append(resumes, import_bookmarks=False)
    if os.path.exists(resume_book_path):
        os.remove(resume_book_path)
    if not os.path.exists(resume_book_path):
        merger.write(resume_book_path)
    merger.close()


def get_name(user_id):
    query = """
    SELECT first_name, preferred_name FROM members where user_id=%s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        result = cursor.fetchone()
    res = result[
        "preferred_name"] if result["preferred_name"] is not None and result["preferred_name"] != "" else result[
            "first_name"]
    return res


def get_email(user_id):
    query = """
    SELECT email FROM users where user_id=%s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        result = cursor.fetchone()
    return result["email"]

def get_waiver(user_id, waiver_type):
    query = "SELECT user_id, first_name, preferred_name, middle_name, last_name, " + waiver_type + "_path FROM members NATURAL JOIN " + waiver_type +" where user_id = %s"
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        res = cursor.fetchone()
    if res == None:
        res = {}
    res[waiver_type+'_url'] = generate_waiver_url(res.get(waiver_type+'_path', ''), waiver_type)
    return res

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
    date_of_birth, phone, school, major, degree_type, graduation_year, 
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
    result['resume_url'] = generate_resume_url(result['resume'])
    dt = date.fromisoformat(str(result['date_of_birth']))
    result['is_18'] = 'YES' if app_year.dob_threshold > dt else 'NO'
    return result


def get_status(user_id):
    """
    Using the user_id, returns the status and reimbursement amount for a user
    """
    query = """
    SELECT status, reimbursement_amt FROM users NATURAL JOIN status NATURAL JOIN applications WHERE
    user_id = %s AND application_year = %s
    """

    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id, app_year.year + "0000"])
        result = cursor.fetchone()
    return result

def get_waiver_status(user_id, waiver_type):
    query = """
    SELECT {0}_status FROM {0} where user_id = %s""".format(waiver_type)
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [user_id])
        result = cursor.fetchone()
    return result

def generate_resume_url(resume_name):
    """
    Given a resume_name, generates the resume url
    """
    if resume_name is not None:
        return flask.url_for("judging.uploaded_file", filename=resume_name)
    return ""

def generate_waiver_url(waiver_name, waiver_type):
    """
    Given a waiver_name, generates the waiver url
    """
    if waiver_name is not "":
        return flask.url_for("judging.uploaded_waiver_file", filename=waiver_name, waiver_type=waiver_type)
    return ""

def get_waiver_name(email):
    uid = auth_utils.get_user_id(email)
    query = """ SELECT waiver_path FROM caltech_waiver WHERE user_id = %s"""
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [uid])
        res = cursor.fetchone()
    return res.get('waiver_path', "")

def get_all_application_links():
    """
    Returns a list which contains a dictionary. 
    This dictionary contains the name, user_id, status, and link
    to their view applications page. 
    """
    result = []
    query = """
    SELECT user_id, first_name, last_name, status 
    FROM members NATURAL JOIN status"""
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [])
        result = cursor.fetchall()
    for i in result:
        i['link'] = flask.url_for(
            "judging.view_application", user_id=i['user_id'], _external=True)
    return result

def get_all_waiver_links():
    result = []
    query = """
    SELECT rsvped_user.user_id    AS user_id,
       rsvped_user.first_name AS first_name,
       rsvped_user.last_name  AS last_name,
       waiver.caltech_waiver_status   AS caltech_waiver_status,
       med_form.medical_info_status AS medical_info_status
FROM   (SELECT user_id,
               first_name,
               last_name
        FROM   status
               NATURAL JOIN members
        WHERE  status = "rsvped") AS rsvped_user
       LEFT JOIN (SELECT user_id,
                         caltech_waiver_status
                  FROM   caltech_waiver) AS waiver
              ON rsvped_user.user_id = waiver.user_id
       LEFT JOIN (SELECT user_id,
                         medical_info_status
                  FROM   medical_info) AS med_form
              ON rsvped_user.user_id = med_form.user_id
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [])
        result = cursor.fetchall()
    for i in result:
        i['link'] = flask.url_for(
            "judging.view_caltech_waiver", user_id=i['user_id'], _external=True)
    return result

def get_current_stats(limit=6):
    """
    Returns some statistics from the db. 
    """
    stats = {}
    query = """
    SELECT status, COUNT(*) FROM status NATURAL JOIN 
    applications WHERE application_year = %s
    GROUP BY status
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [app_year.year + "0000"])
        res = cursor.fetchall()
    stats["status"] = reorder_stat(res, "status")
    cats = [
        "shirt_size", "school", "major", "degree_type", "graduation_year",
        "in_state", "bus_from", "gender"
    ]
    for cat in cats:
        query = """
        SELECT {0}, COUNT(*) from applications NATURAL JOIN status WHERE application_year = %s AND status = "RSVPed"
        GROUP BY {0} ORDER BY COUNT(*) DESC LIMIT %s 
        """.format(cat)
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [app_year.year + "0000", limit])
            res = cursor.fetchall()
        stats[cat] = reorder_stat(res, cat)

    query = """
    SELECT diet_restrictions, COUNT(*) FROM diet NATURAL JOIN applications NATURAL JOIN status 
    WHERE application_year = %s AND status = "RSVPed"
    GROUP BY diet_restrictions
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [app_year.year + "0000"])
        res = cursor.fetchall()
    stats['diet'] = reorder_stat(res, "diet_restrictions")

    query = """
    SELECT race_type, COUNT(*) FROM race NATURAL JOIN applications NATURAL JOIN status
    WHERE application_year = %s AND status = "RSVPed"
    GROUP BY race_type
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [app_year.year + "0000"])
        res = cursor.fetchall()
    stats['race'] = reorder_stat(res, "race_type")

    query = """
    SELECT COUNT(*) FROM applications
    WHERE application_year = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [app_year.year + "0000"])
        res = cursor.fetchall()
    stats['total_applications'] = res[0]['COUNT(*)']

    query = """
    SELECT COUNT(*) FROM users
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchall()
    stats['total_users'] = res[0]['COUNT(*)']
    return stats


def reorder_stat(res, col_name):
    """
    Redordering such that we have a label (ie, XS, S, M, L, XL) 
    as the key and the count as the val. 
    """
    labels = []
    data = []
    empty_count = 0
    for i in res:
        if str(i[col_name]) == "NULL" or i[col_name] == None or str(
                i[col_name]) == "":
            empty_count += i['COUNT(*)']
            continue
        labels.append(str(i[col_name]))
        data.append(i['COUNT(*)'])
    if empty_count > 0:
        labels.append("EMPTY")
        data.append(empty_count)
    return {"labels": labels, "data": data}

def update_waiver_status(user_id, new_status, decider_id):
    query = """
    UPDATE caltech_waiver SET waiver_status = %s, reviewer_user_id = %s WHERE user_id = %s
    """
    with flask.g.pymysql_db.cursor() as cursor:
        cursor.execute(query, [new_status, decider_id, user_id])
    #TODO: email them

def update_status(user_id, new_status, reimbursement_amount, decider_id=None):
    """
    Given a user_id and a status, update the status in the status
    table. 
    """
    if reimbursement_amount == "None":
        reimbursement_amount = None
    if decider_id is None:
        query = """
        UPDATE status SET status = %s, reimbursement_amt = %s WHERE user_id = %s
        """
        with flask.g.pymysql_db.cursor() as cursor:
            cursor.execute(query, [new_status, reimbursement_amount, user_id])
    else:
        if reimbursement_amount != None:
            query = """
            UPDATE status SET reimbursement_amt = %s, decider_user_id = %s WHERE user_id = %s
            """
            with flask.g.pymysql_db.cursor() as cursor:
                cursor.execute(query,
                               [reimbursement_amount, decider_id, user_id])
        else:
            query = """
            UPDATE status SET status = %s, decider_user_id = %s WHERE user_id = %s
            """
            with flask.g.pymysql_db.cursor() as cursor:
                cursor.execute(query, [new_status, decider_id, user_id])
    first_name = get_name(user_id)
    email = get_email(user_id)
    if reimbursement_amount is not None and new_status == "Accepted":
        subject = "Reimbursement Information"
        msg = email_templates.ReimbursementEmail.format(
            first_name, reimbursement_amount)
        email_utils.send_email(email, msg, subject, gmail=True)
    elif new_status == "Accepted":
        subject = "Congratulations! You've Been Accepted!"
        msg = email_templates.AcceptedEmail.format(first_name)
        email_utils.send_email(email, msg, subject, gmail=True)
    elif new_status == "Rejected":
        subject = "Hacktech Application Update"
        msg = email_templates.RejectedEmail.format(first_name)
        email_utils.send_email(email, msg, subject, gmail=True)
