# app/__init__.py
from flask import Flask
from config import Config
from .api.v1.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .api import create_api
    create_api(app)
    
    return app
