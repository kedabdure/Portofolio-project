# app/api/v1/endpoints.py
from flask import jsonify
from .. import api_v1


@api_v1.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, All World!"})

@api_v1.route('/goodbye', methods=['GET'])
def goodbye():
    return jsonify({"message": "Goodbye, World!"})