from flask import Blueprint

# Define the blueprint
main = Blueprint('main', __name__)

# Import the routes to register them with the blueprint
from . import main_routes, api_routes
