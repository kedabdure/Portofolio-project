from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")


    from .main import main
    from .form import auth

    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
