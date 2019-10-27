import flask
blueprint = flask.Blueprint('applications', __name__, template_folder='templates')

import hacktech.modules.applications.routes
