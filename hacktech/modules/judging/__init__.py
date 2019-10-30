import flask
blueprint = flask.Blueprint('judging', __name__, template_folder='templates')

import hacktech.modules.judging.routes
