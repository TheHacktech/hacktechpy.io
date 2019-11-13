"""
Tests hacktech/modules/judging/
"""

import flask
import pytest
from hacktech.testing.fixtures import client
from hacktech import app

from hacktech.modules.judging import routes, helpers
from hacktech.modules.applications import helpers as app_helpers


def test_judging_routes(client):
    # Redirect since the user is not an admin
    assert client.get(flask.url_for('judging.judge')).status_code == 302
    assert client.get(flask.url_for('judging.view_application',
                                    user_id=1)).status_code == 302
    assert client.get(flask.url_for('judging.show_stats')).status_code == 302

    with client.session_transaction() as sess:
        sess['username'] = 'zmo@yahoo.com'
        sess['admin'] = True
    # Now that we are logged in, the pages should load.
    assert client.get(flask.url_for('judging.judge')).status_code == 200
    assert client.get(flask.url_for('judging.view_application',
                                    user_id=1)).status_code == 200
    assert client.get(flask.url_for('judging.show_stats')).status_code == 200


def test_judging_helpers(client):
    res = helpers.get_application(-1)
    assert res == None
    all_applications = helpers.get_all_application_links()
    assert len(all_applications) == 5
    # None admin should never be able to see applications
    assert client.get(all_applications[1]['link']).status_code == 302

    with client.session_transaction() as sess:
        sess['username'] = 'zmo@yahoo.com'
        sess['admin'] = True
    assert client.get(all_applications[1]['link']).status_code == 200

    # False since this is an admin account
    app = helpers.get_application(1)
    assert app == None

    app = helpers.get_application(2)
    assert app['user_id'] == 2
    assert app['first_name'] == 'Juliette'
    assert app['last_name'] == 'Hu'
    assert app['preferred_name'] == 'Julietto-sama'
    assert app['school'] == 'Caltech'

    email = "jmu@caltech.edu"
    assert not app_helpers.check_accepted(email, email)

    helpers.update_status(email, "Accepted")
