from . import main
from flask import render_template, url_for, redirect, Blueprint
from flask_login import login_required, current_user

main = Blueprint("main", __name__)

# HOME
@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def index():
    return render_template('index.html')

# SERVICES
@main.route('/services', methods=['GET'])
def services():
    return redirect(url_for('main.index') + '#services')

# REGISTER
@main.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

