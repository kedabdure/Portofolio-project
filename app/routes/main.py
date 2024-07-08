from . import main
from flask import render_template, url_for, redirect, request
from flask_login import login_required, current_user
from app.models.models import User, Booking


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

# ADMIN ROUTE
@main.route('/admin')
@login_required
def admin():
    """Admin dashboard"""
    if current_user.is_admin:
        bookings = Booking.query.all()  # Retrieve all bookings
        users = User.query.all()  # Retrieve all users (if needed)
        return render_template('dashboard.html', users=users, bookings=bookings)  # Pass bookings to the template
    return redirect(url_for('auth.login'))
