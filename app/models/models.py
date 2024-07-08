from app import db
from datetime import datetime
from flask_login import UserMixin
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

    def __repr__(self):
        return f"User(id={self.id}, fullname='{self.first_name} {self.last_name}', phone='{self.phone}', email='{self.email}', date_created='{self.date_created}')"


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_location = db.Column(db.String(200), nullable=False)
    street_name = db.Column(db.String(200), nullable=False)
    task_size = db.Column(db.String(100), nullable=True)  # Allow nullable for optional field
    task_detail = db.Column(db.Text, nullable=False)
    full_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    service_name = db.Column(db.String(200), nullable=True)  # Optional service name field
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Booking {self.id} - {self.full_name}>'
