import flask

from hacktech.modules.applications import blueprint, helpers

@blueprint.route("/applications")
def applications():
    # TODO: pre-fill with already existing information!
    return flask.render_template("applications.html")

@blueprint.route("/applications/update")
def update_applications():
    return flask.redirect(flask.url_for("home"))
