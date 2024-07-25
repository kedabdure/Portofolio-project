import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    DEBUG = os.getenv('DEBUG', 'False')
    API_URL = os.getenv('API_URL', 'http://your-api-url.com/api/v1')
    ADMIN_PASWORD = os.getenv('ADMIN_PASWORD', '')
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', '')
    PORT=os.getenv('PORT', '5000')
    HOST=os.getenv('HOST', '0.0.0.0')
    ADMIN_DASHBOARD_URL=os.getenv('ADMIN_DASHBOARD_URL', '')
    
    
    # print("ADMIN_PASWORD: {}".format(ADMIN_PASWORD))
    # print("API_URL: {}".format(API_URL))
    # print("SECRET_KEY: {}".format(SECRET_KEY))