from flask import render_template, url_for, redirect, Blueprint, session
from flask_login import login_required, current_user

main = Blueprint("main", __name__)

# HOME
@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def index():
    user = session.get('user')
    return render_template('index.html', user=user)

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
