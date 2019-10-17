import flask

from hacktech.testing.fixtures import client
from hacktech import app


def test_home(client):
    rv = client.get(flask.url_for('home'))

    assert rv.status_code == 200
