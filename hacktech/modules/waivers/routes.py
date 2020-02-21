import flask
import os
from hacktech import auth_utils
from hacktech.modules.waivers import blueprint, helpers
import json
from hacktech.modules.judging import helpers as judging_helpers

@blueprint.route("/waivers")
def waivers():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    return flask.render_template(
        "waivers.html",
        RSVPed = True,
        caltech_waiver=helpers.submitted_caltech_waiver(email),
        medical_info=helpers.submitted_medical_info(email))


@blueprint.route("/waivers/caltech_waiver")
def caltech_waiver():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    status = helpers.submitted_caltech_waiver(email)
    form_info = judging_helpers.get_waiver(auth_utils.get_user_id(email))
    form_info['waiver_name'] = form_info['waiver_url'].split("/")[-1]
    return flask.render_template(
        "caltech_waiver.html", form_info=form_info)

@blueprint.route("/waivers/medical_information")
def medical_information():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    status = helpers.submitted_medical_info(email)
    return flask.render_template("medical_info.html", status=status)

def general_waiver():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    status = helpers.submitted_caltech_waiver(email)
    form_info = judging_helpers.get_waiver(auth_utils.get_user_id(email))
    form_info['waiver_name'] = form_info['waiver_url'].split("/")[-1]
    return flask.render_template(
        "caltech_waiver.html", form_info=form_info)

@blueprint.route("/waivers/update_caltech_waivers", methods=["POST"])
def update_caltech_waiver():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    if 'caltech_waiver' in flask.request.files:
        waiver_file = flask.request.files['caltech_waiver']
    else:
        flask.flash("Please upload your filled waiver!")
        flask.redirect(flask.url_for(".caltech_waiver"))

    helpers.save_caltech_waiver(email, waiver_file, "WAIVERS", "caltech_waivers")
    flask.flash("Thanks for submitted a waiver! A Hacktech organizer will view and make sure that your waiver is complete")
    return flask.redirect(flask.url_for(".waivers"))

@blueprint.route("/waivers/update_medical_information", methods=["POST"])
def update_medical_information():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    if 'medical_information' in flask.request.files:
        waiver_file = flask.request.files['medical_information']
    else:
        flask.flash("Please upload your filled medical information!")
        flask.redirect(flask.url_for(".medical_information"))

    helpers.save_caltech_waiver(email, waiver_file, "MEDICAL", "medical_info")
    flask.flash("Thanks for submitting your medical information! A Hacktech organizer will view and make sure that your info is complete")
    return flask.redirect(flask.url_for(".waivers"))

