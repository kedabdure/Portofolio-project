import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    DEBUG = os.getenv('DEBUG', 'False')
    API_URL = os.getenv('API_URL', 'http://your-api-url.com/api/v1')
    
    
    print("DEBUG: {}".format(DEBUG))
    print("API_URL: {}".format(API_URL))
    # print("SECRET_KEY: {}".format(SECRET_KEY))