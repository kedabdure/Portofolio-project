# app/api/v1/endpoints.py
from flask import jsonify
from .. import api_v1

@api_v1.route('/', methods=['GET'])
@api_v1.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, Welcome Ex.Handyman Services!"})

@api_v1.route('/goodbye', methods=['GET'])
def goodbye():
    return jsonify({"message": "Goodbye, World!"})
