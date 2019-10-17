"""Default website configurations, used only for testing.
"""

from hacktech import environment

# Public Test Database
TEST = environment.Environment(
    db_hostname="localhost",
    db_name="hacktech_test",
    db_user="hacktech_test",
    db_password="public",
    debug=True,
    testing=True,
    secret_key="1234567890")
