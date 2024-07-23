from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import requests
from config import Config

auth = Blueprint("auth", __name__)


def check_email_exists(email):
    """
    Check if the given email already exists in the database via the API.

    Args:
        email (str): The email to check.

    Returns:
        bool: True if the email exists, False otherwise.
    """
    try:
        response = requests.get(f"{Config.API_URL}/api/v1/users")
        response.raise_for_status()  # Check for HTTP errors
        users = response.json()
        user = next((u for u in users if u['email'] == email), None)
        return user is not None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Handle user sign-up requests.

    Renders the sign-up page and processes form submissions to create a new user.
    Validates form input, checks if the email already exists, and submits the new user data to the API.
    """
    if request.method == 'POST':
        # Collect form data
        formData = request.form
        first_name = formData.get('first_name')
        last_name = formData.get('last_name')
        phone = formData.get('phone')
        email = formData.get('email')
        password1 = formData.get('password1')
        password2 = formData.get('password2')

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
            if check_email_exists(email):
                flash('Email address already exists', category='error')
            else:
                data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'phone': phone,
                    'email': email,
                    'password': generate_password_hash(password1, method='pbkdf2:sha256'),  # Hash the password
                }
                response = requests.post(f"{Config.API_URL}/api/v1/users", json=data)

                # Check the response from the API
                if response.status_code == 201:
                    flash('Registration successful', 'success')
                    return redirect(url_for('main.index'))
                else:
                    flash('Registration failed', 'error')
    
    return render_template('signup.html', user=current_user)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = {
            'email': request.form['email'],
            'password': request.form['password']
        }
        response = requests.post("{}/login".format(Config.API_URL), json=data)  # Fix: Use dot notation
        if response.status_code == 200:
            session['user'] = response.json()
            flash('Login successful', 'success')
            return redirect(url_for('main.profile'))
        else:
            flash('Login failed', 'danger')
    return render_template('login.html')

