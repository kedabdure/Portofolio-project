from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

from api.v1.views import api_views as api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api/v1')


@app.errorhandler(404)
def page_not_found(error):
    """custom page not found msg"""
    message = {"error": "Not found"}
    return jsonify(message), 404


# run the flask app
if __name__ == '__main__':
    app.run(debug=True)