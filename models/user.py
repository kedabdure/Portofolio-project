from datetime import datetime
from flask_login import UserMixin
from . import db
import uuid


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    is_admin = db.Column(db.Boolean, default=False) # no user is now an admin, if its false

    # to dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'date_created': self.date_created,
            'is_admin': self.is_admin,
        }
        

    def __repr__(self):
        return f"User(id={self.id}, fullname='{self.first_name} {self.last_name}', phone='{self.phone}', email='{self.email}', date_created='{self.date_created}')"
