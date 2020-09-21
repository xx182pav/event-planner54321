from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Email, Length,ValidationError, EqualTo
from .models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=4, max=100)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Войти")

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EventsForm(FlaskForm):
    author = StringField('Author')
    theme = StringField('Theme')
    description = StringField('Description')
    start_time = DateTimeLocalField('Start_time',format="%Y-%m-%dT%H:%M")
    end_time = DateTimeLocalField('End_time', format="%Y-%m-%dT%H:%M")
    submit = SubmitField('Go')


       