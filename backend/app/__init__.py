# app/__init__.py
from flask import Flask
from config import Config
from flask_cors import CORS
from .api.v1.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app) # allow all route

    with app.app_context():
        db.create_all()

    from .api import create_api
    create_api(app)

    return app
