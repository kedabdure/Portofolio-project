from . import db
from datetime import datetime


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
    status = db.Column(db.String, default='Pending')

    def to_dict(self):
        """booking obj to dictionary"""
        return {
            'id': self.id,
            'task_location': self.task_location,
            'street_name': self.street_name,
            'task_size': self.task_size,
            'task_detail': self.task_detail,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone,
            'service_name': self.service_name,
            'date_created': self.date_created,
            'status': self.status
        }


    def __repr__(self):
        return f'<Booking {self.id} - {self.full_name}>'


    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)


    # EXAMPLAE OF POST, PUT BOOKING
    # curl -X PUT -H "Content-Type: application/json" -d '{"email": "ekram@shemsu"}' http://127.0.0.1:5000/api/v1/booking/2
    # curl -X POST -H "Content-Type: application/json" -d '{"task_location": "Location 3", "street_name": "Street 3", "task_size": "Medium", "task_detail": "Task 3 details", "full_name": "Michael Brown", "email": "michael.brown@example.com", "phone": "5555555555"}' http://127.0.0.1:5000/api/v1/bookin
