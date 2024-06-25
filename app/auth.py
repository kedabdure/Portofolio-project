from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Login successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('main.services'))
            else:
                flash("Incorrect Password!", category='error')
        else:
            flash("Email does't exist", category='error')

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        data = request.form
        name = data.get('full_name')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if not name or len(name) <= 2:
            flash("Name must be greater than 2 characters", category='error')
        elif not email or len(email) < 3:
            flash('Email must be greater than 3 characters', category='error')
        elif not password1 or len(password1) < 4:
            flash('Password must be greater than 4 characters', category='error')
        elif not password2 or len(password2) < 4:
            flash('Password must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        else:
            new_user = User(email=email, full_name=name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account successfully created!', category='success')
            return redirect(url_for('main_route.home'))

    return render_template('sign_up.html', user=current_user)
