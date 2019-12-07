import flask
import os
from hacktech import auth_utils
from hacktech.modules.applications import blueprint, helpers
from werkzeug.utils import secure_filename


@blueprint.route("/applications")
def applications():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    return flask.render_template(
        "applications.html",
        schools=helpers.get_schools(),
        majors=helpers.get_majors(),
        form_info=helpers.get_form_info(email),
        submitted=(helpers.check_submitted(email, email)))


@blueprint.route("/applications/rsvp")
def rsvp():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()

    accepted = helpers.check_accepted(flask.session['username'],
                                      flask.session['username'])
    return flask.render_template("rsvp.html", accepted=accepted)


@blueprint.route("/applications/status")
def status():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()

    status = helpers.check_status(flask.session['username'],
                                  flask.session['username'])
    return flask.render_template("dashboard.html", status=status)


@blueprint.route("/applications/update_status", methods=["POST"])
def update_status():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    helpers.update_status(email,
                          flask.request.form.get("RSVPed")
                          or flask.request.form.get("Declined"))
    print(flask.request.form.get("RSVPed"))
    print(flask.request.form.get("Declined"))
    return flask.redirect(flask.url_for(".status"))


@blueprint.route("/applications/update", methods=["POST"])
def update_applications():
    """Handles an application update request."""
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    action = flask.request.form.get("Submit") or flask.request.form.get("Save")
    email = flask.session['username']
    first_name = flask.request.form.get("firstName", None)
    middle_name = flask.request.form.get("middleName", None)
    last_name = flask.request.form.get("lastName", None)
    preferred_name = flask.request.form.get("preferredName", None)
    phone_number = flask.request.form.get("phoneNumber", None)
    school = flask.request.form.get("school", None)
    major = flask.request.form.get("major", None)
    degree_type = flask.request.form.get("degreeType", None)
    graduation_year = flask.request.form.get("graduationYear", None)
    github = flask.request.form.get("github", None)
    linkedin = flask.request.form.get("linkedin", None)
    
    # Special cases for major and school not in options
    if school == "N/A" or not school:
        school = flask.request.form.get("school_opt", None)
    if major == "N/A" or not major:
        school = flask.request.form.get("major_opt", None)
        
    # Check if the request has a resume attached
    resume = ""
    resume_file = None
    resume_name = ""
    last_resume_name = helpers.check_resume_exists(helpers.get_user_id(email))
    print(last_resume_name)
    if 'resume' in flask.request.files:
        resume_file = flask.request.files['resume']
        # Make sure user selected file
        if action == 'Submit' and resume_file.filename == '' and not last_resume_name:
            flask.flash('Please upload your resume.')
            return flask.redirect(flask.url_for("applications.applications"))
    if resume_file and helpers.allowed_file(resume_file):
        resume_name = secure_filename(resume_file.filename)
        resumes_root_path = os.path.join(flask.current_app.root_path,
                               flask.current_app.config['RESUMES'])
        resume_name = resume_name.split(".")
        resume_name = secure_filename(str(resume_name[:-1]) + '_' +str(helpers.get_user_id(email)) + ".pdf")

        resume_file.save(
            os.path.join(resumes_root_path, resume_name))
    elif action == 'Submit' and not last_resume_name:
        flask.flash(
            'Please make sure your resume is a PDF file less than 500 KB.')
        return flask.redirect(flask.url_for("applications.applications"))

    if resume_name == "":
        resume_name = last_resume_name 
    latino = flask.request.form.get("latino", None)
    race = flask.request.form.getlist("race", None)
    gender = flask.request.form.get("gender", None)
    shirt_size = flask.request.form.get("shirtSize", None)
    need_transportation = flask.request.form.get("needTransportation", None)
    bus_from = flask.request.form.get("busFrom", None)
    airport = flask.request.form.get("airport", None)
    dietary_restrictions = flask.request.form.get("dietaryRestrictions", None)
    diet_choices = flask.request.form.getlist("dietaryRestrictionsChoices",
                                              None)
    diet_details = flask.request.form.get("dietaryRestrictionsDetail", None)
    q1 = flask.request.form.get("Q1", None)
    q2 = flask.request.form.get("Q2", None)
    q3 = flask.request.form.get("Q3", None)
    q4 = flask.request.form.get("Q4", None)
    code_of_conduct = flask.request.form.get("codeOfConduct", None)

    
    success, msg = helpers.handle_update_applications(
        action, email, phone_number, school, major, degree_type,
        graduation_year, github, linkedin, resume_name, latino, race, gender,
        shirt_size, need_transportation, bus_from, airport,
        dietary_restrictions, diet_choices, diet_details, q1, q2, q3, q4,
        code_of_conduct, first_name, middle_name, last_name, preferred_name)
    # Display message from application update
    flask.flash(msg)
    if not success:
        return flask.redirect(flask.url_for("applications.applications"))
    return flask.redirect(flask.url_for("home"))
