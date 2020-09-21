import os
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from werkzeug.debug import DebuggedApplication



from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
login.init_app(app)
bcrypt = Bcrypt(app)



from app import routes, models, forms

db.create_all()

