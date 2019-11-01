  
import flask

from hacktech.modules.judging import blueprint, helpers
from hacktech import auth_utils

@blueprint.route("/judge")
def judge():
    if not auth_utils.check_admin():
        return flask.redirect(flask.url_for("home"))
    info = helpers.get_all_application_links()
    return flask.render_template("judge.html", info=info)


@blueprint.route("/view_application/<int:user_id>")
def view_application(user_id):
    if not auth_utils.check_admin():
        return flask.redirect(flask.url_for("home"))
    info = helpers.get_application(user_id)
    return flask.render_template("view_application.html", info=info)
