from models import db
from datetime import datetime
from flask_login import UserMixin

# The following methods are provided by UserMixin:
# which are allowing user sessions to be managed correctly:-
# is_authenticated
# is_active
# is_anonymous
# get_id: return user's primary_key

class User(db.Model, UserMixin):
    __tablename__ = 'user'  # Make sure this matches your table name
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'date_created': self.date_created,
        }

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)


# EXAMPLE OF DELETE, POST AND GET METHODS FOR API
# curl -X DELETE http://127.0.0.1:5000/api/v1/users/1
# curl -X GET http://127.0.0.1:5000/api/v1/users or /users/1
# curl -X POST -H "Content-Type: application/json" -d '{"first_name": "fuad", "last_name": "hassen", "email": "fuad.johnson@example.com", "phone": "222222222", "password": "1111"}' http://127.0.0.1:5000/api/v1/users