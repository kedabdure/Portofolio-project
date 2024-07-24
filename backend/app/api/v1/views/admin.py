from flask import request, jsonify
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db, Admin
from .. import api_v1


# GET ALL USERS
@api_v1.route('/admins', methods=['GET'], strict_slashes=False)
def get_admins():
    """Retrieves the list of all User objects"""
    users = Admin.query.all()
    return jsonify([user.to_dict() for user in users])


# SINGUP
@api_v1.route('/admins/signup', methods=['POST'])
def admin_signup():
    data = request.get_json()

    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')
    

    # Validate received data (basic example)
    if not all([first_name, last_name, email, phone, password]):
        return jsonify({"error": "Missing data"}), 400

    # Check if user already exists
    if Admin.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    # Hash the password
    password=generate_password_hash(password, method='pbkdf2:sha256')

    # Create new admin
    new_admin = Admin(
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
        print('admin crated successfully', new_admin)
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Something went wrong"}), 500


# LOGIN
@api_v1.route('/admins/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    admin = Admin.query.filter_by(email=email).first()
    
    if admin and check_password_hash(admin.password, password):
        login_user(admin)
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401


# LOGOUT
@api_v1.route('/admins/logout', methods=['POST'])
@login_required
def admin_logout():
    logout_user()
    return jsonify({"success": True, "message": "Logout successful"})
