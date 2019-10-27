PasswordChangedEmail = \
"""Hi {0},\n
Your password has been successfully changed. If you did not request a password
change, please let us know immediately at devteam@hacktech.caltech.edu.\n
Thanks!
hacktech Devteam
"""

ResetPasswordEmail = \
"""Hi {0},\n
We have received a request to reset this account's password. If you didn't
request this change, let us know immediately at devteam@hacktech.caltech.edu. Otherwise,
you can use this link to change your password:
{1}
Your link will expire in {2}.\n
Thanks!
hacktech Devteam
"""

ResetPasswordSuccessfulEmail = \
"""Hi {0},\n
Your password has been successfully reset. If you did not request a password
reset, please let us know immediately at devteam@hacktech.caltech.edu.\n
Thanks!
hacktech Devteam
"""

AddedToWebsiteEmail = \
"""Hi {0},\n
You have been added to the hacktech website. In order to access private
areas of our site, please complete registration by creating an account here:
{1}
If you have any questions or concerns, please find us or email us at devteam@hacktech.caltech.edu.\n
Thanks!
hacktech Devteam
"""

CreateAccountRequestEmail = \
"""Hi {0},\n
To create an account on the hacktech website, please use this link:
{1}
If you did not initiate this request, please let us know immediately at devteam@hacktech.caltech.edu.\n
Thanks!
hacktech Devteam
"""

CreateAccountSuccessfulEmail = \
"""Hi {0},\n
Your hacktech account has been created. If this
was not you, please let us know immediately.\n
Please confirm your email by going to this link {1}
Thanks!
Hacktech team
"""

MembersAddedEmail = \
"""The following members have been added to the hacktech website:
{0}
and the following members were skipped (they were already in the database):
{1}
You should run the email update script to add the new members.
Thanks!
hacktech Devteam
"""

ErrorCaughtEmail = \
"""An exception was caught by the website. This is probably a result of a bad
server configuration or bugs in the code, so you should look into this. This
was the exception:
{0}
"""
