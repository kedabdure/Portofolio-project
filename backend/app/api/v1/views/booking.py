from flask import jsonify, request, abort
from ..models import db, Booking
from .. import api_v1



# GET ALL BOOKINGS
@api_v1.route('/bookings', methods=['GET'], strict_slashes=False)
def get_bookings():
    """Retrieves the list of all Booking objects"""
    bookings = Booking.query.all()
    booking_list = [booking.to_dict() for booking in bookings]  # I have a to_dict method in my Booking model
    return jsonify(booking_list)


# GET BOOKING BY ID
@api_v1.route('/bookings/<int:book_id>', methods=['GET'], strict_slashes=False)
def get_booking(book_id):
    """Retrieves Booking object by Id"""
    booking = Booking.query.get(book_id)
    if booking is None:
        abort(404)
    return jsonify(booking.to_dict())


# DELETE BOOKING BY ID
@api_v1.route('/bookings/<int:book_id>', methods=['DELETE'], strict_slashes=False)
def delete_booking(book_id):
    """Retrieves Booking object by Id and delete"""
    booking = Booking.query.get(book_id)
    if booking is None:
        abort(404)

    db.session.delete(booking)
    db.session.commit()
    return jsonify({'message': 'Booking deleted successfully'}), 200


# CREATE BOOKING
@api_v1.route('/bookings', methods=['POST'], strict_slashes=False)
def post_booking():
    """Post Booking object"""
    if not request.json:
        abort(404)
    data = request.json  # Get JSON data from request
    # Create a new Booking object from the JSON data
    new_booking = Booking(**data) # the `**data` syntax unpacks the data dictionary, passing its key-value pairs as keyword arguments to the Booking constructor
    db.session.add(new_booking)
    db.session.commit()
    return jsonify(new_booking.to_dict()), 201


# UPDATE BOOKING DATA
@api_v1.route('/bookings/<int:book_id>', methods=['PUT'], strict_slashes=False)
def update_booking(book_id):
    """UPDATE Booking object"""
    booking = Booking.query.get(book_id)
    if booking is None:
        abort(404)
    if not request.json:
        abort(400)
    data = request.get_json()
    booking.update(data)
    db.session.commit()
    return jsonify(booking.to_dict()), 200


# COUNT TASKS
@api_v1.route('/bookings/task_counts', methods=['GET'], strict_slashes=False)
def get_task_counts():
    """Return counts of tasks based on their status"""
    completed_count = Booking.query.filter_by(status='Completed').count()
    pending_count = Booking.query.filter_by(status='Pending').count()
    in_progress_count = Booking.query.filter_by(status='Progressing').count()

    return jsonify({
        'completed': completed_count,
        'pending': pending_count,
        'in_progress': in_progress_count
    }), 200
