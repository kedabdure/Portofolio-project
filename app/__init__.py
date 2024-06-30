from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# from flask_migrate import Migrate
# from flask_bootstrap import Bootstrap
# migrate = Migrate()

# create db instance
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config') # Load configuration setting from specific class

    db.init_app(app) # initialize db with flask app instance


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # specify the login view to redirect when login needed
    login_manager.init_app(app) # bind loginManager instance to Flask app

    from .models import User

    with app.app_context(): # allow flask config info and and other properties accessible globaly in the block which it defined
        db.create_all()     # cuz create all need to access the current state of the app


    @login_manager.user_loader # telling login manager to use the decorated function to load user from database by by id
    def load_user(user_id):    # help for user session management
        return User.query.filter_by(id=user_id)

    #registering blue prints to flask routs
    from app.routes import main as main_blueprint
    from .auth import auth as authentication_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')
    app.register_blueprint(authentication_blueprint, url_prefix='/')

    return app


def create_db(app):
    if not os.path.exists(DB_NAME): # check if the file is already exists
        db.create_all(app=app)
        print('db created success!')
