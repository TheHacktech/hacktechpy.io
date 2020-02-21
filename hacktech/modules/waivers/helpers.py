import flask
from hacktech import auth_utils
from hacktech import app_year
import hacktech.modules.judging.helpers as judging_helpers
from werkzeug.utils import secure_filename
import os


def submitted_caltech_waiver(email):
    pass


def submitted_medical_info(email):
    pass


def fill_caltech_waiver(email, first_name, middle_name, last_name,
                        name_of_participant, phone_number, address, state,
                        zip_code, city, passwd, signature):
    pass


def get_date_month():
    pass


def check_name(first_name, middle_name, last_name, name_of_participant,
               signature):
    first_name = first_name.lower()
    middle_name = middle_name.lower()
    last_name = last_name.lower()
    name_of_participant = name_of_participant.lower()
    signature = signature.lower()

    if name_of_participant == first_name + " " + last_name:
        return True
    if signature == first_name + " " + last_name:
        return True


def fill_medical_info(email, diet, allergy, medical_condition, medicine,
                      emergency_name, emergency_relation, emergency_phone,
                      emergency_alt_phone, physician_name, physician_phone,
                      insurance_company, insurance_phone, insurance_policy,
                      insurance_preauth, insurance_detail):
    pass
