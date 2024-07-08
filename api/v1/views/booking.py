#!/usr/bin/python3
"""
Booking file for API
"""
from api.v1.views import api_views
from flask import abort, jsonify, request, make_response
from models.booking import Booking
from models import db


@api_views.route('/booking', methods=['GET'], strict_slashes=False)
def get_bookings():
    """Retrieves the list of all Booking objects"""
    bookings = Booking.query.all()
    booking_list = [booking.to_dict() for booking in bookings]  # I have a to_dict method in my Booking model
    return jsonify(booking_list)


@api_views.route('/booking/<int:book_id>', methods=['GET'], strict_slashes=False)
def get_booking(book_id):
    """Retrieves Booking object by Id"""
    booking = Booking.query.filter_by(id=book_id).first()
    if booking is None:
        abort(404)
    return jsonify(booking.to_dict())


@api_views.route('/booking/<int:book_id>', methods=['DELETE'], strict_slashes=False)
def delete_booking(book_id):
    """Retrieves Booking object by Id and delete"""
    booking = Booking.query.filter_by(id=book_id).first()
    if booking is None:
        abort(404)
    
    db.session.delete(booking)
    db.session.commit()
    return jsonify({'message': 'Booking deleted successfully'}), 200
