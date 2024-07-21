import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '4b65832e5d7c0f2445a0c3f9e50713422c9f0e8e2dce9301'
