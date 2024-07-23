# run.py
from flask import jsonify
from app import create_app

app = create_app()


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


if __name__ == '__main__':
    app.run()
