from flask_cors import CORS
from flask import Flask, jsonify
from api.v1.views import api_views
from api.v1.views import mail

app = Flask(__name__)
app.config.from_object('api_config.APIConfig')
mail.init_app(app)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(api_views, url_prefix='/api/v1')


@app.errorhandler(404)
def page_not_found(error):
    """custom page not found msg"""
    message = {"error": "Page Not found"}
    return jsonify(message), 404


# run the flask app
if __name__ == '__main__':
    app.run(debug=True)