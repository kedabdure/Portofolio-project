from flask import render_template, url_for, redirect, Blueprint, session, request, flash
from flask_login import login_required, current_user
from config import Config

main = Blueprint("main", __name__)

# HOME
@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def index():
    user = session.get('user')
    admin = session.get('admin')
    print(admin)
    return render_template('index.html', user=user, admin=admin)

# SERVICES
@main.route('/services', methods=['GET'])
def services():
    return redirect(url_for('main.index') + '#services')

# REGISTER
@main.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

# PROFILE
@main.route('/profile', methods=['GET'])
# @login_required
def profile():
    user = session.get('user')
    return render_template('profile.html', user=user)


@main.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == Config.ADMIN_USERNAME and password == Config.ADMIN_PASWORD:
            session['admin'] = username
            return redirect(url_for('main.index'))
        else:
            flash("Incorrect password or username! Enter the correct credential!", category="error")
    return render_template('admin_login.html')


# Admin
@main.route('/admin', methods=['GET'])
def admin():
    if not session.get('admin'):
        return redirect(url_for('main.admin_login'))
    return redirect(Config.ADMIN_DASHBOARD_URL)


@main.route('/admin-logout')
def admin_logout():
    """
    handle admin logout
    """
    session.pop('admin', None)
    flash('You have been logged out. See you next time! 😊', category='success')
    return redirect(url_for('main.index'))