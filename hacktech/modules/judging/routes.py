import flask

from hacktech.modules.judging import blueprint, helpers
from hacktech import auth_utils
from hacktech.modules.applications import helpers as app_helpers
import os
import json


@blueprint.route("/judge")
def judge():
    curpage = int(flask.request.args.get('page', 0))
    page_size = flask.session.get('page_size', 100)
    if page_size == "":
        page_size = 100
    else:
        page_size = int(page_size)
    flask.session['page_size'] = page_size
    if not auth_utils.check_login() or not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    info = helpers.get_all_application_links()
    total_pages = int(len(info) / page_size) + 1
    info = info[curpage * page_size:(curpage + 1) * page_size]
    return flask.render_template(
        "judge.html",
        info=info,
        page=curpage,
        total_pages=total_pages,
        page_size=page_size)


@blueprint.route("/update_page_size", methods=['POST'])
def update_page_size():
    flask.session['page_size'] = flask.request.form.get('page_size', 100)
    if flask.session['page_size'] == "":
        flask.session['page_size'] = 100
    flask.session['page_size'] = int(flask.session['page_size'])
    return flask.redirect(flask.url_for("judging.judge"))


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
    if not auth_utils.check_login():
        return flask.redirect(flask.url_for("home"))

    user_res_name = app_helpers.check_resume_exists(
        app_helpers.get_user_id(flask.session['username']))

    if user_res_name != filename and not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    uploads = os.path.join(flask.current_app.root_path,
                           flask.current_app.config['RESUMES'])
    return flask.send_from_directory(uploads, filename, as_attachment=False)


@blueprint.route('/judge/resumes', methods=['POST'])
def serve_resume_book():
    if not auth_utils.check_login() or not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    fields = flask.request.form.getlist("groups", None)
    if fields == None:
        return flask.redirect(flask.url_for("judging.judge"))

    helpers.generate_resume_book(fields)
    return flask.redirect(
        flask.url_for(
            "judging.uploaded_file", filename="hacktech_resume_book.pdf"))


@blueprint.route('/judge/update/<int:user_id>', methods=['POST'])
def update_status(user_id):
    if not auth_utils.check_login() or not auth_utils.check_admin(
            flask.session['username']):
        return flask.redirect(flask.url_for("home"))
    helpers.update_status(user_id,
                          flask.request.form.get('new_status'),
                          flask.request.form.get('reimbursement_amount'),
                          app_helpers.get_user_id(flask.session['username']))
    flask.flash('Status has been updated')
    return flask.redirect(flask.url_for('judging.judge'))
