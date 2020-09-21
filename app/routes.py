from random import randint
from .config import Config
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from flask import jsonify, render_template, request, redirect, flash, g, url_for, session, logging
from app import app, db, login
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash 
from .models import User, Events
from flask_login import current_user, login_user, login_required, logout_user
from .forms import LoginForm, RegistrationForm, EventsForm
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError




@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
        # @app.route('/index', methods = ['POST', 'GET'])
    user = db.session.query(User.username)
    form = EventsForm()
    if request.method == 'POST':
        # form.validate_on_submit()  
        author = request.form.get("author")
        theme = request.form.get("theme")
        description = request.form.get("description")
        start_time = request.form.get("start_time")
        start_format = datetime.strptime(start_time, "%Y-%m-%dT%H:%M")
        end_time = request.form.get("end_time")
        end_format = datetime.strptime(end_time, "%Y-%m-%dT%H:%M")
        even = Events(author=author,theme=theme,description=description, 
        start_time=start_format,end_time=end_format)
        db.session.add(even)
        db.session.commit()
        return redirect(url_for('events'))
    return render_template('index.html', user=user, form=form)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/events', methods=['GET', 'POST'])
def events():
    even_all = db.session.query(Events.author, Events.theme, Events.description, Events.start_time, Events.end_time)
    
    # return redirect(url_for('index'))
    return render_template('events.html', even=even_all)
    


# @app.route('/edit/<int:edit_id>', methods=['GET', 'POST'])
# def event_update(edit_id):
#     event = db.session.query(Events).filter(Events._id==int(edit_id)).first()
#     event_form = EventsForm()
#     if request.method == 'POST':
#         author = request.form.get('author')
#         if author != _id:
#             error = "Forbidden event to edit"
#             return render_template('error.html',form=event_form, error = error)
#     start_time = request.form.get('start_time')
#     start_format = datetime.strptime(start_time,'%Y-%m-%dT%H:%M')
#     end_time = request.form.get('end_time')
#     end_format = datetime.strptime(end_time,'%Y-%m-%dT%H:%M')
#     theme = request.form.get('theme')
#     description = request.form.get('description')
#     event.author = author
#     event.theme = theme
#     event.description = description
#     event.start_time = start_format
#     event.end_time = end_format
#     db.session.commit()
#     return redirect(url_for('index'))
#     return render_template('error.html',form=event_form)
#     return render_template('edit.html', form=event_form)

@app.route('/edit', methods=['POST','GET'])
def edit():
    event = db.session.query(Events.author, Events.theme, Events.description, Events.start_time, Events.end_time).all()
    form = EventsForm()
    if request.method == 'POST':
            # form.validate_on_submit()
        # author=request.form.get("author")
        # if author == author:
        #     return 'Error edit event'  
        #     theme = request.form.get("theme")
        #     description = request.form.get("description")
        #     start_time = request.form.get("start_time")
        #     start_format = datetime.strptime(start_time, "%Y-%m-%dT%H:%M")
        #     end_time = request.form.get("end_time")
        #     end_format = datetime.strptime(end_time, "%Y-%m-%dT%H:%M")
        #     event.theme = theme
        #     event.description = description
        #     event.start_time = start_format
        #     event.end_time = end_format
            # db.session.add(theme, description, start_time, end_time)
            # db.session.commit()
            return redirect(url_for('index'))
    return render_template('edit.html', form=form)

















