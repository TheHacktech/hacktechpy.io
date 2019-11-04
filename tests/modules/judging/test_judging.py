"""
Tests hacktech/modules/judging/
"""

import flask
import pytest
from hacktech.testing.fixtures import client
from hacktech import app

from hacktech.modules.judging import routes, helpers


def test_judging_routes(client):
    # Redirect since the user is not an admin
    assert client.get(flask.url_for('judging.judge')).status_code == 302

    with client.session_transaction() as sess:
        sess['username'] = 'zmo@yahoo.com'
        sess['admin'] = True

    assert client.get(flask.url_for('judging.judge')).status_code == 200


def test_judging_helpers(client):
    res = helpers.get_application(-1)
    assert res == None
