from app import db
from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import uuid


# User model/table
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  # Unique user ID
    first_name = db.Column(db.String(50), nullable=False)  # First name of the user
    last_name = db.Column(db.String(120), nullable=True)  # Last name of the user
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email for the user
    phone = db.Column(db.String(15), nullable=False)  # Phone number of the user
    password = db.Column(db.String(128), nullable=False)  # Password for the user account
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)  # Account creation date

    bookings = db.relationship('Booking', backref='user', lazy=True)  # Relationship with the Booking model

    def __repr__(self):
        return f"User(id={self.id}, fullname='{self.first_name} {self.last_name}', phone='{self.phone}', email='{self.email}', date_created='{self.date_created}')"


# Service model/table
class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)  # Unique service ID
    service_name = db.Column(db.String(200), nullable=False)  # Name of the service
    service_detail = db.Column(db.String(1000), nullable=False)  # Details about the service
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)  # Service creation date

    bookings = db.relationship('Booking', backref='service', lazy=True)  # Relationship with the Booking model


# Booking model/table
class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)  # Unique booking ID
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User model
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)  # Foreign key to Service model
    booking_date = db.Column(db.DateTime, nullable=False)  # Date of booking
    status = db.Column(db.String(50), nullable=False)  # Status of the booking
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)  # Booking creation date
    
    # new field to store picture url or path
    picture = db.Column(db.String(255), nullable=True)