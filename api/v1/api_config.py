import os

class APIConfig:
    API_KEY = os.environ.get('API_KEY') or 'default-api-key'
    # BASE_URL = os.environ.get('API_BASE_URL') or 'http://localhost:5000/api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://abdure:1234@localhost/database'
    
    # MAIL CONFIGURATION
    MAIL_SERVER = "smtp.fastmail.com"
    MAIL_PORT = 587
    MAIL_USERNAME = "experthandyman@fastmail.com"
    MAIL_PASSWORD = "9u547n6a8p4z343g"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False