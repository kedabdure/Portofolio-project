import sys
import os
from flask_cors import CORS
from flask import Flask, jsonify
from api.v1.views import mail
from models import db

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

try:
    app.config.from_object('api_config.APIConfig')
    from api.api_config import APIConfig
    print("Import successful")
except ImportError as e:
    print("Not successful")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# CONNECT API TO DB AND MAIL
db.init_app(app)
mail.init_app(app)

# REGISTER BLUEPRINT
from api.v1.views import api_views
app.register_blueprint(api_views, url_prefix='/api/v1')

@app.errorhandler(404)
def page_not_found(error):
    """Custom page not found message"""
    message = {"error": "Page Not Found"}
    return jsonify(message), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom internal server error message"""
    message = {"error": "Internal Server Error"}
    return jsonify(message), 500

# Run the Flask app
if __name__ == '__main__':
    app.run()
