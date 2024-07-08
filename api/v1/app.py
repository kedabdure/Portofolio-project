#!/usr/bin/python3
"""
Flask app
"""
from flask import Flask, jsonify
from views import app_views
from models import db

app = Flask(__name__)
app.register_blueprint(app_views)
db.init_app(app)

@app.errorhandler(404)
def page_not_found(error):
    """custom page not found msg"""
    message = {"error": "Not found"}
    return jsonify(message), 404


if __name__ == "__main__":
    app.run(debug=True)
