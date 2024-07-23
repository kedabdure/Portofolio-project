from flask import Blueprint, render_template, request, flash, redirect, url_for, session, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import requests
from config import Config

auth = Blueprint("auth", __name__)


# CHECK EMAIL
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


# SIGNUP
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
                # Post the data
                response = requests.post(f"{Config.API_URL}/api/v1/users", json=data)

                if response.status_code == 201:
                    # Fetch user data for session management
                    user_response = requests.get(f"{Config.API_URL}/api/v1/users/email/{email}")
                    if user_response.status_code == 200:
                        user_data = user_response.json()
                        print(user_data)
                        session['user'] = user_data  # Store user data in session
                        flash('Registration successful', 'success')
                        return redirect(url_for('main.index'))
                    else:
                        flash('Failed to retrieve user data after registration', 'error')
                else:
                    flash('Registration failed', 'error')

    return render_template('signup.html', user=current_user)



# LOGIN
@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle user login requests.

    Renders the login page and processes form submissions to authenticate the user.
    Checks the user credentials against the data retrieved from the API.
    """
    if request.method == 'POST':
        # Collect form data
        formData = request.form
        email = formData.get('email')
        password = formData.get('password')

        # Check if the email exists
        if check_email_exists(email):
            try:
                # Fetch users from API
                response = requests.get(f"{Config.API_URL}/api/v1/users")
                response.raise_for_status()  # Check for HTTP errors
                users = response.json()
                
                # Find the user by email
                user = next((u for u in users if u['email'] == email), None)
                
                # Check if the password matches
                if check_password_hash(user['password'], password):
                    session['user'] = user
                    flash('Login successful! 😊', category='success')
                    return redirect(url_for('main.index'))
                else:
                    flash('Incorrect password! 😡', category='error')
                    # return redirect(url_for('auth.login'))
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                flash('Error fetching users from API', category='danger')
                return redirect(url_for('auth.login'))
        else:
            flash('Email doesn\'t exist! 😔', category='error')
            return redirect(url_for('auth.login'))
    
    return render_template('login.html', user=current_user)


@auth.route('/logout')
# @login_required
def logout():
    """Handle user logout by clearing the session and redirecting to the login page."""
    session.pop('user', None)  # Remove user data from the session
    flash('You have been logged out. See you next time! 😊', category='success')
    return redirect(url_for('main.index'))


@auth.route('/booking', methods=['GET', 'POST'])
def booking():
    """
    Handle booking requests.

    Renders the booking page and processes form submissions to create a new booking.
    Validates the form data and sends it to the API for storage.
    """
    service_title = request.args.get('service_title', default='', type=str)
    booking_success = False

    if request.method == 'POST':
        # Collect form data
        formData = request.form
        service_name = formData.get('service_name')
        task_location = formData.get('task_location')
        street_name = formData.get('street_name')
        task_size = formData.get('task_size')
        task_detail = formData.get('task_detail')
        full_name = formData.get('full_name')
        email = formData.get('email')
        phone = formData.get('phone')

        # Validate the form data
        if not full_name or len(full_name) <= 2:
            flash("Full name must be greater than 2 characters", category='error')
        elif not email or len(email) < 3:
            flash('Email must be greater than 3 characters', category='error')
        elif not phone or len(phone) < 10:
            flash('Phone number must be at least 10 characters', category='error')
        elif not task_location:
            flash('Task location is required', category='error')
        elif not service_name:
            flash('Service name is required', category='error')
        elif not street_name:
            flash('Street name is required', category='error')
        elif not task_detail:
            flash('Task detail is required', category='error')
        else:
            # Prepare data for the API
            data = {
                'service_name': service_name,
                'task_location': task_location,
                'street_name': street_name,
                'task_size': task_size,
                'task_detail': task_detail,
                'full_name': full_name,
                'email': email,
                'phone': phone
            }

            try:
                # Send data to the API
                response = requests.post(f"{Config.API_URL}/api/v1/bookings", json=data)
                response.raise_for_status()  # Check for HTTP errors

                if response.status_code == 201:
                    # flash('Booking successful!', category='success')
                    booking_success = True
                    return redirect(url_for('main.index') + '?success=true')
                else:
                    flash('Booking failed', category='danger')
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                flash('Error while booking. Please try again later.', category='danger')

    return render_template('booking.html', user=current_user, booking_success=booking_success, service_title=service_title)