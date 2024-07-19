from flask import request, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from . import api_views
from app import db
from models import Admins


# SINGUP
@api_views.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')

    # Validate received data (basic example)
    if not all([first_name, last_name, email, password]):
        return jsonify({"error": "Missing data"}), 400

    # Check if user already exists
    if Admins.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    # Hash the password
    password=generate_password_hash(password, method='pbkdf2:sha256')

    # Create new admin
    new_admin = Admins(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        password=password
    )

    # Add new admin to the database
    try:
        db.session.add(new_admin)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Something went wrong"}), 500


# LOGIN
@api_views.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    admin = Admins.query.filter_by(email=email).first()
    
    if admin and check_password_hash(admin.password, password):
        login_user(admin)
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

# LOGOUT
@api_views.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"success": True, "message": "Logout successful"})
