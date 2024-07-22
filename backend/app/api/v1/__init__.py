# app/api/v1/__init__.
from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

from .views.endpoints import *
from .views.booking import *
from .views.user import *
