from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    """users note table"""
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # many to one relationship

class User(db.Model, UserMixin):
    """User table model"""
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    notes = db.relationship('Note', backref='user', lazy=True)  # one to many relationship
    
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(150), nullable=False)
    service_detail = db.Column(db.String(1000), nullable=False)
