import flask
from flask import jsonify
from hacktech import app
from hacktech.auth_utils import get_user_id
from hacktech.constants import CONTACTS


@app.route('/')
def home():
    return flask.render_template('hacktech.html')


@app.route('/schedule')
def schedule():
    return flask.render_template('schedule.html')
