import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError as e:
    print("faild to import", e)


class Config:
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # Print to verify the variables are loaded correctly
    # print("DEBUG: {}".format(DEBUG))
    # print("SECRET_KEY: {}".format(SECRET_KEY))
    print("SQLALCHEMY_DATABASE_URI: {}".format(SQLALCHEMY_DATABASE_URI))
