import os

class Config:
    # DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    
    # MAIL CONFIGURATION
    MAIL_SERVER = "smtp.fastmail.com"
    MAIL_PORT = 587
    MAIL_USERNAME = "experthandyman@fastmail.com"
    MAIL_PASSWORD = "9u547n6a8p4z343g"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False