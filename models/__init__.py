from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .booking import Booking
from .admins import Admins