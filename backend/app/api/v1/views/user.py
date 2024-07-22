from flask import jsonify, request, abort
from .. import api_v1
from ..models import db, User


# GET ALL USERS
@api_v1.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


# GET USER BY ID
@api_v1.route('/users/<int:user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object"""
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


# DELETE USER BY ID
@api_v1.route('/users/<int:user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    db.session.delete(user)
    db.session.commit()
    return jsonify({}), 204


# CREATE USER
@api_v1.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a User object"""
    if not request.json:
        abort(400)
    data = request.get_json()
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201


# UPDATE USER DATA
@api_v1.route('/users/<int:user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a User object"""
    user = User.query.get(user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    user.update(data)
    db.session.commit()
    return jsonify(user.to_dict())
