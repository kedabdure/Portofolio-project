from flask import Blueprint

api_views = Blueprint('app_views', __name__) 

from api.v1.views.users import *
from api.v1.views.booking import *
