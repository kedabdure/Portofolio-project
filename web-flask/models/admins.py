from models import db
from datetime import datetime
from flask_login import UserMixin


class Admins(db.Model, UserMixin):
    __tablename__ = 'admins'  # Make sure this matches your table name
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