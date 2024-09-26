# app/api/v1/endpoints.py
from flask import jsonify
from .. import api_v1

@api_v1.route('/', methods=['GET'])
@api_v1.route('/hello', methods=['GET'])
def hello():
    """
    This function returns a JSON response with a welcome message.

    The function is designed to handle GET requests at the root ('/') and '/hello' endpoints.
    It returns a JSON response with a 'message' key containing a welcome message.

    Parameters:
    None

    Returns:
    dict: A JSON response with a 'message' key containing the welcome message.
    """
    return jsonify({"message": "Hello, Welcome Ex.Handyman Services!"})


@api_v1.route('/goodbye', methods=['GET'])
def goodbye():
    """
    This function returns a JSON response with a goodbye message.

    Parameters:
    None

    Returns:
    dict: A JSON response with a 'message' key containing the goodbye message.
    """
    return jsonify({"message": "Goodbye, World!"})
