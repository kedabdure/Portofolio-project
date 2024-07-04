from . import main
from flask import render_template, url_for, redirect
from flask_login import login_required, current_user


@main.route('/', methods=['GET'])
@main.route('/home', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/services', methods=['GET'])
def services():
    return redirect(url_for('main.index') + '#services')


@main.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@main.route('/profile')
@login_required
def profile():
    # Mock data for bookings
    bookings = [
        {'date': '2024-01-15', 'service': 'Plumbing', 'status': 'Completed'},
        {'date': '2024-02-20', 'service': 'Electrical', 'status': 'Pending'},
        {'date': '2024-03-10', 'service': 'Cleaning', 'status': 'Cancelled'}
    ]

    return render_template('user_profile.html', user=current_user, bookings=bookings)


@main.route('/booking')
def booking():
    """booking section"""
    return render_template('booking.html')

