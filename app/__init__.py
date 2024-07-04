from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
import os

# Create db instance
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Load configuration settings from a specific class

    db.init_app(app)  # Initialize db with Flask app instance

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Specify the login view to redirect when login is needed
    login_manager.init_app(app)  # Bind LoginManager instance to Flask app

    from app.models.models import User  # Import User model

    @app.context_processor
    def inject_user():
        return dict(user=current_user)  # Inject the current user into the template context

    with app.app_context():  # Access Flask config and other properties globally within this block
        db.create_all()  # Create all tables in the database

    @login_manager.user_loader  # Load user by ID for session management
    def load_user(user_id):
        return User.query.get(user_id)  # As the id in db model is string no need to convert it to Integer int(user_id)

    # Register blueprints to Flask routes
    from app.routes.main import main as main_blueprint
    from app.routes.auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')  # Add a prefix for auth routes

    return app

def create_db(app):
    if not os.path.exists(DB_NAME):  # Check if the database file already exists
        db.create_all(app=app)  # Create all tables in the database
        print('Database created successfully!')
