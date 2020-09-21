from app import db 
from sqlalchemy import *
from app import login
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Events(db.Model):
    __tablename__ = 'events'
    _id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20),unique = True, nullable=False)
    theme = db.Column(db.String(50), unique = True, nullable=False)
    description = db.Column(db.String(300), unique = True, nullable=True)
    start_time = db.Column(db.DateTime, unique = True, nullable=False)
    end_time = db.Column(db.DateTime, unique = True, nullable=False)

    def __init__(self, author, theme, description, start_time, end_time):
        self.author = author
        self.theme = theme
        self.description = description
        self.start_time = start_time
        self.end_time = end_time





