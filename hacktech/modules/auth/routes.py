import flask
from hacktech import auth_utils, constants
from hacktech.modules.auth import blueprint, helpers
from hacktech.modules.auth.permissions import Permissions
from hacktech.modules.judging import helpers as judging_helpers


@blueprint.route('/login')
def login():
    """Display login page."""
    return flask.render_template('login.html')


@blueprint.route('/login/submit', methods=['POST'])
def login_submit():
    """Handle authentication."""
    username = flask.request.form.get('username', None)
    password = flask.request.form.get('password', None)

    if username is not None and password is not None:
        user_id = helpers.authenticate(username, password)
        if user_id is not None:
            flask.session['username'] = username
            if auth_utils.check_admin(username):
                flask.session['admin'] = True

            # Update last login time
            auth_utils.update_last_login(username)
            flask.session['status'] = judging_helpers.get_status(user_id)[
                'status']
            # Return to previous page if in session
            if 'next' in flask.session:
                redirect_to = flask.session.pop('next')
                return flask.redirect(redirect_to)
            else:
                return flask.redirect(flask.url_for('home'))
    flask.flash('Incorrect username or password. Please try again!')
    return flask.redirect(flask.url_for('auth.login'))


@blueprint.route('/login/forgot')
def forgot_password():
    """Displays a form for the user to reset a forgotten password."""
    return flask.render_template('forgot_password.html')


@blueprint.route('/login/forgot/submit', methods=['POST'])
def forgot_password_submit():
    """Handle forgotten password submission."""
    email = flask.request.form.get('email', None)

    helpers.handle_forgotten_password(email)
    flask.flash(
        "An email with a recovery link has been sent, if that email exists")
    return flask.redirect(flask.url_for('auth.login'))


@blueprint.route('/login/reset/<reset_key>')
def reset_password(reset_key):
    """Checks the reset key. If successful, displays the password reset prompt."""
    username = auth_utils.check_reset_key(reset_key)
    if username is None:
        flask.flash(
            'Invalid request. If your link has expired, then you will need to generate a new one. '
            'If you continue to encounter problems, please contact devteam@hacktech.caltech.edu.'
        )
        return flask.redirect(flask.url_for('auth.forgot_password'))
    return flask.render_template(
        'reset_password.html', username=username, reset_key=reset_key)


@blueprint.route('/login/reset/<reset_key>/submit', methods=['POST'])
def reset_password_submit(reset_key):
    """Handles a password reset request."""
    username = auth_utils.check_reset_key(reset_key)
    if username is None:
        # Reset key was invalid.
        flask.flash("Someone's making it on the naughty list this year...")
        return flask.redirect(flask.url_for('auth.forgot_password'))
    new_password = flask.request.form.get('password', '')
    new_password2 = flask.request.form.get('password2', '')
    if helpers.handle_password_reset(username, new_password, new_password2):
        flask.flash('Password reset was successful.')
        return flask.redirect(flask.url_for('auth.login'))
    else:
        # Password reset handler handles error flashes.
        return flask.redirect(
            flask.url_for('auth.reset_password', reset_key=reset_key))


@blueprint.route('/logout')
def logout():
    flask.session.pop('username', None)
    flask.session.pop('admin', None)
    return flask.redirect(flask.url_for('home'))
