from flask import Blueprint, jsonify


api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@api_v1.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})


@api_v1.route('/goodbye', methods=['GET'])
def goodbye():
    return jsonify({"message": "Goodbye, World!"})
