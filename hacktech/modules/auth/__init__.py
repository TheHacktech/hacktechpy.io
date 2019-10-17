import flask
blueprint = flask.Blueprint('auth', __name__, template_folder='templates')

import hacktech.modules.auth.routes
