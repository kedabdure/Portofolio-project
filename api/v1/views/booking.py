#!/usr/bin/python3
"""
Booking file for API
"""
from views import app_views
from flask import abort, jsonify, request, make_response
from models.booking import Booking
from models import db


@app_views.route('/booking', methods=['GET'], strict_slashes=False)
def get_booking():
    """Retrieves the list of all User objects"""
    bookings = Booking.query.all()
    booking_list = [booking.to_dict() for booking in bookings]  # I have a to_dict method in my User model
    return jsonify(booking_list)


# @app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
# def get_user(user_id):
#     """Retrieves a User object"""
#     user = User.query.filter_by(id=user_id).first()
#     if user is None:
#         abort(404)
#     return jsonify(user.to_dict())


# @app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
# def delete_user(user_id):
#     """Deletes a User object"""
#     user = User.query.filter_by(id=user_id).first()
#     if user is None:
#         abort(404)

#     db.session.delete(user)
#     db.session.commit()
#     return jsonify({'message': 'User deleted successfully'}), 200