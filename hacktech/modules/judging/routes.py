import flask

from hacktech.modules.judging import blueprint, helpers
from hacktech import auth_utils


@blueprint.route("/judge")
def judge():
    if not auth_utils.check_login() or not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    info = helpers.get_all_application_links()
    return flask.render_template("judge.html", info=info)


@blueprint.route("/view_application/<int:user_id>")
def view_application(user_id):
    if not auth_utils.check_login() or not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    info = helpers.get_application(user_id)
    return flask.render_template("view_application.html", info=info)


@blueprint.route("/stats")
def show_stats():
    if not auth_utils.check_login() or not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    return flask.render_template("stats.html")


@blueprint.route('/judge/update/<int:user_id>', methods=['POST'])
def update_status(user_id):
    if not auth_utils.check_login() or not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    helpers.update_status(user_id, flask.request.form.get('new_status'))
    flask.flash('Status has been updated')
    return flask.redirect(flask.url_for('judging.judge'))
