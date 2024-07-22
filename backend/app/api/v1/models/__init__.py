# backend/api/v1/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .admin import Admin
from .booking import Booking
from .user import User
