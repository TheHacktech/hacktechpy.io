'''
Use this file to store names for global permissions -- permissions
that don't belong in any particular module. 

For module specific permissions, create an Enum within the module
'''

import enum
from hacktech import environment

# Test Database
TEST = environment.Environment(
    db_hostname="localhost",
    db_name="hacktech_test",
    db_user="hacktech_test",
    db_password="",
    debug=False,
    testing=False,
    secret_key="111",
    em="12334",
    email="122222"
)


class Permissions(enum.IntEnum):
    #Site admins -- always have permission to everything -- Use with caution
    ADMIN = 1
