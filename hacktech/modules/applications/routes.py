import flask
import os
from hacktech import auth_utils
from hacktech.modules.applications import blueprint, helpers
from werkzeug.utils import secure_filename

@blueprint.route("/applications")
def applications():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    # TODO: pre-fill with already existing information!
    return flask.render_template("applications.html")


@blueprint.route("/applications/rsvp")
def rsvp():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()

    accepted = helpers.check_accepted(flask.session['username'])
    return flask.render_template("rsvp.html", accepted=accepted)


@blueprint.route("/applications/update", methods=["POST"])
def update_applications():
    """Handles an application update request."""
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    phone_number = flask.request.form.get("phoneNumber", None)
    school = flask.request.form.get("school", None)
    major = flask.request.form.get("major", None)
    degree_type = flask.request.form.get("degreeType", None)
    graduation_year = flask.request.form.get("graduationYear", None)
    github = flask.request.form.get("github", None)
    linkedin = flask.request.form.get("linkedin", None)
    # Check if the request has a resume attached
    # todo: finish error-handling for submit flow (redirect)
    # if 'resume' not in flask.request.files:
    #    flask.flash('Please attach a resume.')
    resume = None
    if 'resume' in flask.request.files:
        resume = flask.request.files['resume']
         # Make sure user selected file
        if resume.filename == '':
            flash('No selected file')
            # todo: redirect
    if resume and helpers.allowed_file(resume.filename):
        filename = secure_filename(resume.filename)
        resumes = os.path.join(flask.current_app.root_path,
                           flask.current_app.config['RESUMES'])
        resume.save(os.path.join(resumes, filename))
    resume = flask.request.form.get("resume", None)
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

    success, error_msg = helpers.handle_update_applications(
        email, phone_number, school, major, degree_type, graduation_year,
        github, linkedin, resume, latino, race, gender, shirt_size,
        need_transportation, bus_from, airport, dietary_restrictions,
        diet_choices, diet_details, q1, q2, q3, q4, code_of_conduct)
    if success:
        flask.flash("Your application has been submitted!")
    else:
        flask.flash(error_msg)
        return flask.redirect(flask.url_for("applications.applications"))
    return flask.redirect(flask.url_for("home"))
