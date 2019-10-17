import smtplib
from email.mime.text import MIMEText


def send_email(to, msg, subject, use_prefix=True):
    """
  Sends an email to a user. Expects 'to' to be a comma separated string of
  emails, and for 'msg' and 'subject' to be strings.
  """
    msg = MIMEText(msg)

    if use_prefix and '[ASCIT hacktech]' not in subject:
        subject = '[ASCIT hacktech] ' + subject

    msg['Subject'] = subject
    msg['From'] = 'auto@hacktech.caltech.edu'
    msg['To'] = to

    s = smtplib.SMTP('localhost')
    s.sendmail('auto@hacktech.caltech.edu', [to], msg.as_string())
    s.quit()
