from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return "Hello, All World!"
    return app
