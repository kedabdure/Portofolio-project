from flask import Flask, current_app
from flask_login import LoginManager, current_user
import requests
from config import Config

def create_app():
    """
    Create and configure the Flask application.

    This function sets up the Flask app, initializes Flask-Login, and registers blueprints.
    """
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Specify the login view for redirects
    login_manager.init_app(app)  # Bind LoginManager instance to the app

    # Inject the current user into the template context
    @app.context_processor
    def inject_user():
        return dict(user=current_user)

    # User loader function
    @login_manager.user_loader
    def load_user(user_id):
        """
        Load a user by their ID using an API call.

        :param user_id: The ID of the user to load.
        :return: User data if found, else None.
        """
        try:
            response = requests.get(f"{Config.API_URL}/users/{user_id}")
            response.raise_for_status()  # Check for HTTP errors
            user_data = response.json()
            if user_data:
                return user_data  # Return user data directly
            return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while loading user: {e}")
            return None

    # Register blueprints
    from .main import main
    from .form import auth

    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
