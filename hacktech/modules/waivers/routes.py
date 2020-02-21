import flask
import os
from hacktech import auth_utils
from hacktech.modules.waivers import blueprint, helpers
import json


@blueprint.route("/waivers")
def waivers():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    return flask.render_template(
        "waivers.html",
        caltech_waiver=helpers.submitted_caltech_waiver(email),
        medical_info=helpers.submitted_medical_info(email))


@blueprint.route("/waivers/caltech_waiver")
def caltech_waiver():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    status = helpers.submitted_caltech_waiver(email)
    return flask.render_template(
        "caltech_waiver.html", validations={}, form_info={}, curdate={})


@blueprint.route("/waivers/medical_information")
def medical_information():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    status = helpers.submitted_medical_info(email)
    return flask.render_template("medical_info.html", status=status)


@blueprint.route("/waivers/update_caltech_waivers", methods=["POST"])
def update_caltech_waiver():
    if not auth_utils.check_login():
        return auth_utils.login_redirect()
    email = flask.session['username']
    first_name = flask.request.form.get("firstName", None)
    middle_name = flask.request.form.get("middleName", None)
    last_name = flask.request.form.get("lastName", None)
    name_of_participant = flask.request.form.get("nameOfParticipant", None)
    phone_number = flask.request.form.get("phoneNumber", None)
    address = flask.request.form.get("streetAddress", None)
    state = flask.request.form.get("state", None)
    zip_code = flask.request.form.get("zipcode", None)
    city = flask.request.form.get("city", None)
    passwd = flask.request.form.get("password", None)
    signature = flask.request.form.get("signature", None)
    helpers.fill_caltech_waiver(email, first_name, middle_name, last_name,
                                name_of_participant, phone_number, address,
                                state, zip_code, city, passwd, signature)
    return flask.redirect(flask.url_for(".waiver"))


@blueprint.route("/waivers/update_medical_information", methods=["POST"])
def update_medical_information():
    """Handles an application update request."""
    if not auth_utils.check_login():
        return auth_utils.login_redirect()

    email = flask.session['username']

    diet = flask.request.form.get("diet", None)
    allergy = flask.request.form.get("allergy", None)
    medical_condition = flask.request.form.get("medicalCondition", None)
    medicine = flask.request.form.get("medicine", None)
    emergency_name = flask.request.form.get("emergencyName", None)
    emergency_relation = flask.request.form.get("emergencyRelation", None)
    emergency_phone = flask.request.form.get("emergencyPhone", None)
    emergency_alt_phone = flask.request.form.get("emergencyAltPhone", None)
    physician_name = flask.request.form.get("physicianName", None)
    physician_phone = flask.request.form.get("physicianPhone", None)
    insurance_company = flask.request.form.get("insuranceCompany", None)
    insurance_phone = flask.request.form.get("insurancePhone", None)
    insurance_policy = flask.request.form.get("insurancePolicy", None)
    insurance_preauth = flask.request.form.get("insurancePreAuth", None)
    insurance_detail = flask.request.form.get("insuranceDetail", None)

    helpers.fill_medical_info(
        email, diet, allergy, medical_condition, medicine, emergency_name,
        emergency_relation, emergency_phone, emergency_alt_phone,
        physician_name, physician_phone, insurance_company, insurance_phone,
        insurance_policy, insurance_preauth, insurance_detail)
    return flask.redirect(flask.url_for(".waiver"))
