import flask

from hacktech import auth_utils
from hacktech.modules.account import blueprint, helpers


@blueprint.route("/create")
def create_account():
    """Provides a form to confirm an account."""
    return flask.render_template("request_account.html")


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

    if email is None or password is None or password2 is None or first_name is None or last_name is None:
        flask.flash("Invalid request.")
        return flask.redirect(flask.url_for("account.create_account"))
    success, error_msg = helpers.handle_create_account(
        email, password, password2, first_name, middle_name, preferred_name,
        last_name)
    if success:
        flask.flash("An email has been sent! Please confirm your account.")
    else:
        flask.flash(error_msg)
        return flask.redirect(flask.url_for("account.create_account"))
    return flask.redirect(flask.url_for("home"))

