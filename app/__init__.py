from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_migrate import Migrate # help to modify the db schema 
import os
from models import db
from flask_cors import CORS

# to use flask migration first
# `flask db init` initialize flask migration if the first time 
# then make model change
# Run `flask db migrate -m "Add phone column to User model."` to create a migration script that includes your changes.
# `flask db upgrade` Apply the migration to update the database schema with the new column.


DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Load configuration settings from a specific class
    CORS(app)
    # we can also configure CORS with specific parameters
    # CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})


    db.init_app(app)  # Initialize db with Flask app instance
    migrate = Migrate(app, db) # Initialize Flask-Migrate
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Specify the login view to redirect when login is needed
    login_manager.init_app(app)  # Bind LoginManager instance to Flask app

    from models.user import User  # Import User model

    @app.context_processor
    def inject_user():
        return dict(user=current_user)  # Inject the current user into the template context


    with app.app_context():  # Access Flask config and other properties globally within this block
        db.create_all()  # Create all tables in the database
        user = User.query.filter_by(email='abdurehimk77@gmail.com').first()
        
        if user:
            user.is_admin = True
            db.session.commit()
            print('User promoted successfully!')
        else:
            print("User not found.")


    @login_manager.user_loader  # Load user by ID for session management
    def load_user(user_id):
        return User.query.get(user_id)  # As the id in db model is string no need to convert it to Integer int(user_id)

    # Register blueprints to Flask routes
    from app.routes.main import main as main_blueprint
    from app.routes.form import auth as auth_blueprint
    from api.v1.views import api_views as api_blueprint

    app.register_blueprint(main_blueprint, url_prefix='/')
    app.register_blueprint(api_blueprint, url_prefix='/api/v1') # registering api views
    app.register_blueprint(auth_blueprint, url_prefix='/auth')  # Add a prefix for auth routes

    return app

def create_db(app):
    if not os.path.exists(DB_NAME):  # Check if the database file already exists
        db.create_all(app=app)  # Create all tables in the database
        print('Database created successfully!')
