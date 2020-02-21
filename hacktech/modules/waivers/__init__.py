import flask
blueprint = flask.Blueprint('waivers', __name__, template_folder='templates')

import hacktech.modules.waivers.routes
