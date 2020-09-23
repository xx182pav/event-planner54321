import os
from dotenv import load_dotenv
from configparser import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP="app.py"
    FLASK_DEBUG=1
    FLASK_ENV= 'development'
    SECRET_KEY='very_good_secret_key'


    
   
