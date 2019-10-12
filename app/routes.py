import flask
from flask import render_template, request, jsonify, flash, redirect, url_for
from app import app, db

from flask_login import current_user, login_user, logout_user
from app.models import User

from app.forms import LoginForm, RegistrationForm

from flask_login import logout_user

ROOMS = ["general", "lecture", "homework", "exams", "debug"]

@app.route("/")
def index(): 
    global current_user   
    return render_template('chatroom.html', current_user = current_user, rooms = ROOMS)

@app.route('/register', methods=['GET', 'POST'])
def register():
    print(current_user)
    if current_user.is_authenticated:
        print("user is already registered - take them to the homepage")
        return redirect(url_for('index'))
    print("user needs to register")
    form = RegistrationForm()
    print("form")
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():

        #user = Users.query.get(id)

        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        #login_user(user)


        # this really needs to give some kind of error - like that the user wasn't found.
        return redirect(url_for('index'))
    else:
        return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))