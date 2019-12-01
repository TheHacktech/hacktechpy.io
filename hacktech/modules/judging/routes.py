import flask

from hacktech.modules.judging import blueprint, helpers
from hacktech import auth_utils
import os
import json


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
    status = helpers.get_status(user_id)
    return flask.render_template(
        "view_application.html", info=info, status=status)


@blueprint.route("/stats")
def show_stats():
    if not auth_utils.check_login() or not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    default_stats = helpers.get_current_stats()
    return flask.render_template(
        "stats.html", raw_data=json.dumps(default_stats))


@blueprint.route('/resume/<filename>', methods=['GET'])
def uploaded_file(filename):
    '''
    Serves the actual uploaded file.
    '''
    uploads = os.path.join(flask.current_app.root_path,
                           flask.current_app.config['RESUMES'])
    return flask.send_from_directory(uploads, filename, as_attachment=False)


@blueprint.route('/judge/update/<int:user_id>', methods=['POST'])
def update_status(user_id):
    if not auth_utils.check_login() or not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    helpers.update_status(user_id,
                          flask.request.form.get('new_status'),
                          flask.request.form.get('reimbursement_amount'))
    flask.flash('Status has been updated')
    return flask.redirect(flask.url_for('judging.judge'))
