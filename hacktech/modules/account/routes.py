import flask

from hacktech import auth_utils
from hacktech.modules.account import blueprint, helpers
import json


@blueprint.route("/create")
def create_account():
    """Provides a form to confirm an account."""
    partial = flask.request.args.get("partial", '{"email":"", "first_name":"", "middle_name":"", "preferred_name":"", "last_name":"", "dob":""}')
    partial = json.loads(partial)
    return flask.render_template("request_account.html", partial=partial)


@blueprint.route("/create/submit", methods=["POST"])
def create_account_submit():
    """Handles an account creation request."""
    email = flask.request.form.get("email", None)
    password = flask.request.form.get("password", None)
    password2 = flask.request.form.get("password2", None)
    first_name = flask.request.form.get("first_name", None)
    middle_name = flask.request.form.get("middle_name", None)
    preferred_name = flask.request.form.get("preferred_name", None)
    last_name = flask.request.form.get("last_name", None)
    dob = flask.request.form.get("date_of_birth", None)
    partial = {}
    partial["email"] = email
    partial["first_name"] = first_name
    partial["middle_name"] = middle_name
    partial["preferred_name"] = preferred_name
    partial["last_name"] = last_name
    partial["dob"] = dob
    if email is None or password is None or password2 is None or first_name is None or last_name is None or dob is None or dob == "" or dob == "0000-00-00":
        flask.flash("Make sure you fill out all parts of the form!")
        return flask.redirect(flask.url_for("account.create_account"))
    if not helpers.check_valid_dob(dob):
        flask.flash("Make sure that your birthday is formatted as 2020-03-06")
        return flask.redirect(flask.url_for("account.create_account", partial = json.dumps(partial)))
    if '@' not in email:
        flask.flask("Make sure you enter your email correctly!")
        return flask.redirect(flask.url_for("account.create_account", partial = json.dumps(partial)))
    success, error_msg = helpers.handle_create_account(
        email, password, password2, first_name, middle_name, preferred_name,
        last_name, dob)
    if success:
        flask.flash("You've successfully created an account!")
        flask.session['username'] = email
    else:
        if error_msg != "":
            flask.flash(error_msg)
        return flask.redirect(flask.url_for("account.create_account", partial = json.dumps(partial)))
    return flask.redirect(flask.url_for("home"))
