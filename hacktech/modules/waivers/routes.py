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
    user_id = auth_utils.get_user_id(email)
    return flask.render_template(
        "waivers.html",
        RSVPed = (judging_helpers.get_status(user_id)['status'] == "RSVPed"),
        caltech_waiver=helpers.get_waiver_status(user_id, "caltech_waiver"),
        medical_info=helpers.get_waiver_status(user_id, "medical_info"))


@blueprint.route("/waivers/caltech_waiver")
def caltech_waiver():
    return general_waiver("caltech_waiver", link="https://drive.google.com/file/d/1GjhzwhWJ9EBUyjagxajQFY0dHs_SKAn_/view?usp=sharing", title="CONSENT, RELEASE AND ASSUMPTION OF RISK FOR PARTICIPATION IN HACKTECH AT THE CALIFORNIA INSTITUTE OF TECHNOLOGY March 6-8, 2020")

@blueprint.route("/waivers/medical_information")
def medical_information():
    return general_waiver("medical_info", link="https://drive.google.com/file/d/1fivb6NFmqsSeuIWxov8cNWc8zh8NL2mj/view?usp=sharing", title="MEDICAL INFORMATION DISCLOSURE FOR HACKTECH 2020")

def general_waiver(waiver_type, link, title):
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    # TODO: implement
    #status = helpers.submitted_caltech_waiver(email, waiver_type)
    form_info = judging_helpers.get_waiver(auth_utils.get_user_id(email), waiver_type)
    form_info['waiver_name'] = form_info[waiver_type+'_url'].split("/")[-1]
    form_info['waiver_url'] = form_info[waiver_type+'_url']
    form_info['waiver_update'] = flask.url_for(".update_{0}".format(waiver_type))
    form_info['waiver_type'] = waiver_type
    return flask.render_template(
        "caltech_waiver.html", form_info=form_info, waiver_type=waiver_type, link = link, title=title)

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

    helpers.save_info(email, waiver_file, "WAIVERS", "caltech_waiver")
    flask.flash("Thanks for submitted a waiver! A Hacktech organizer will view and make sure that your waiver is complete")
    return flask.redirect(flask.url_for(".waivers"))

@blueprint.route("/waivers/update_medical_info", methods=["POST"])
def update_medical_info():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    if 'medical_info' in flask.request.files:
        waiver_file = flask.request.files['medical_info']
    else:
        flask.flash("Please upload your filled medical information!")
        flask.redirect(flask.url_for(".medical_information"))

    helpers.save_info(email, waiver_file, "MEDICAL", "medical_info")
    flask.flash("Thanks for submitting your medical information! A Hacktech organizer will view and make sure that your info is complete")
    return flask.redirect(flask.url_for(".waivers"))

