from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


# from flask_migrate import Migrate
# from flask_bootstrap import Bootstrap
# migrate = Migrate()

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    with app.app_context():
        db.create_all()


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id)

    from app.routes import main as main_blueprint
    from .auth import auth as authentication_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')
    app.register_blueprint(authentication_blueprint, url_prefix='/')

    return app


def create_db(app):
    if not os.path.exists(DB_NAME):
        db.create_all(app=app)
        print('db created success!')
