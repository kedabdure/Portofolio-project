from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from app.models.models import User
from app import db
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Check if the form was submitted via POST method
        data = request.form  # Fetch data from the form
        email = data.get('email')  # Get the email from the form data
        password = data.get('password')  # Get the password from the form data

        user = User.query.filter_by(email=email).first()  # Query the user by email from the database

        if user:
            if check_password_hash(user.password, password):  # Verify the user's password
                flash('Login successful!', category='success')  # Flash a success message
                login_user(user, remember=True)  # Log the user in and remember the session
                return redirect(url_for('main.profile'))  # Redirect to the profile page
            else:
                flash("Incorrect password!", category='error')  # Flash an error message
        else:
            flash("Email doesn't exist", category='error')  # Flash an error message if email not found

    return render_template('login.html', user=current_user)  # Render the login template

@auth.route('/logout')
@login_required  # Ensure the user is logged in to access this route
def logout():
    logout_user()  # Log the user out
    return redirect(url_for('main.index'))  # Redirect to the index page

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':  # Check if the form was submitted via POST method
        data = request.form  # Fetch data from the form
        first_name = data.get('first_name')  # Get the first name from the form data
        last_name = data.get('last_name')  # Get the last name from the form data
        phone = data.get('phone')  # Get the phone number from the form data
        email = data.get('email')  # Get the email from the form data
        password1 = data.get('password1')  # Get the first password from the form data
        password2 = data.get('password2')  # Get the second password from the form data

        # Validate the form data
        if not first_name or len(first_name) <= 2:
            flash("First name must be greater than 2 characters", category='error')
        elif not last_name or len(last_name) <= 2:
            flash("Last name must be greater than 2 characters", category='error')
        elif not email or len(email) < 3:
            flash('Email must be greater than 3 characters', category='error')
        elif not phone or len(phone) < 10:
            flash('Phone number must be at least 10 characters', category='error')
        elif not password1 or len(password1) < 4:
            flash('Password must be greater than 4 characters', category='error')
        elif not password2 or len(password2) < 4:
            flash('Password must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        else:
            # Check if the email already exists
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email address already exists', category='error')
            else:
                new_user = User(
                    email=email, 
                    first_name=first_name, 
                    last_name=last_name, 
                    phone=phone, 
                    password=generate_password_hash(password1, method='pbkdf2:sha256')  # Hash the password
                )
                db.session.add(new_user)  # Add the new user to the session
                db.session.commit()  # Commit the session to the database
                login_user(new_user, remember=True)  # Log the new user in
                flash('Account successfully created!', category='success')  # Flash a success message
                return redirect(url_for('main.profile'))  # Redirect to the profile page

    return render_template('sign_up.html', user=current_user)  # Render the sign-up template
