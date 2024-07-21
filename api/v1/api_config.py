from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class APIConfig:
    API_KEY = os.getenv('API_KEY', 'default-api-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://abdure:1234@localhost/database')

    # MAIL CONFIGURATION
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.fastmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your_email@fastmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'default_password')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'False') == 'True'
