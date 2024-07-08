from . import db
from datetime import datetime
from flask_login import UserMixin
import uuid


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