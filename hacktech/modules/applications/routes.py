import flask
import os
from hacktech import auth_utils
from hacktech.modules.applications import blueprint, helpers
import json


@blueprint.route("/applications")
def applications():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    submitted = flask.request.args.get("submit", "")
    majors = helpers.get_majors()
    schools = helpers.get_schools()
    form_info, validations = helpers.get_form_info(email)
    form_info.major_opt = form_info.major if form_info.major not in majors else ""
    form_info.school_opt = form_info.school if form_info.school not in schools else ""
    if form_info.school_opt != "":
        form_info.school = "N/A"
    if form_info.major_opt != "":
        form_info.major = "N/A"
    if submitted != "True":
        validations = helpers.ValidationForm()
    return flask.render_template(
        "applications.html",
        schools=schools,
        majors=majors,
        form_info=form_info,
        submitted=(helpers.check_submitted(email, email)),
        validations=validations.info,
        app_end=True)


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
                          or flask.request.form.get("Declined"), None)
    return flask.redirect(flask.url_for(".status"))


@blueprint.route("/applications/update", methods=["POST"])
def update_applications():
    if True:
        flask.flash("The application period has ended!")
        return flask.redirect(flask.url_for("home"))
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
        school_opt = flask.request.form.get("school_opt", None)
        school = school if school_opt == None or school_opt == "" else school_opt
    if major == "N/A" or not major:
        major = flask.request.form.get("major_opt", None)
    # Check if the request has a resume attached
    resume_file = None
    if 'resume' in flask.request.files:
        resume_file = flask.request.files['resume']

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
    q5 = flask.request.form.get("Q5", None)
    q6 = flask.request.form.get("Q6", None)
    code_of_conduct = (flask.request.form.get("codeOfConduct1", None) == "True") \
            and (flask.request.form.get("codeOfConduct2", None) == "True")
    success, msg = helpers.handle_update_applications(
        action, email, phone_number, school, major, degree_type,
        graduation_year, github, linkedin, resume_file, latino, race, gender,
        shirt_size, need_transportation, bus_from, airport,
        dietary_restrictions, diet_choices, diet_details, q1, q2, q3, q4, q5, q6,
        code_of_conduct, first_name, middle_name, last_name, preferred_name)
    # Display message from application update
    flask.flash(msg)
    return flask.redirect(
        flask.url_for(
            "applications.applications",
            submit=True if action == "Submit" else False))
