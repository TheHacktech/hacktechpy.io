import flask
import pytest
from hacktech.testing.fixtures import client
from hacktech import app
import hacktech.modules.account.helpers as helpers


def test_creating_new_accounts(client):
    # Duplicate email.
    (status, err) = helpers.handle_create_account(
        "wingfrillie@gmail.com", "123456789", "123456789", "Zi", "", "", "Mo")
    assert not status
    assert err == "You already have an account. Try recovering it?"

    (status, err) = helpers.handle_create_account(
        "zmo@caltech.edu", "123456789", "123456789", "Zi", "", "", "Mo")
    assert status
