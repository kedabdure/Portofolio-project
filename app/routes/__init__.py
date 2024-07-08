from flask import Blueprint

# Define the blueprint main routes
main = Blueprint('main', __name__)

# define the blueprint for authentication
auth = Blueprint('auth', __name__)

# Import the routes to register them with the blueprint
from .main import * # this will register all the routes in the main blueprint like index, services, profile...
from .form import * # this will register all the routes in the auth blueprint like login, sign up...
