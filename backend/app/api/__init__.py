# app/api/__init__.py
from flask import Blueprint

def create_api(app):
    from .v1 import api_v1
    app.register_blueprint(api_v1)
