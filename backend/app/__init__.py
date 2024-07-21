# Create app and register all the the blueprints
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .api import create_api
    create_api(app)
    
    return app
