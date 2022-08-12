from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# secures passwords
from werkzeug.security import generate_password_hash, check_password_hash

# define "auth.py" as blueprint of app
auth = Blueprint('auth', __name__)

# define login, logout, sign up using render_template
# can pass in variable as a 2nd argument in render_template function, use it in any other page

# The route below can accept get and post methods


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # look for specific user        
        # query db and filter by all users with the given email. Return first result.
        user = User.query.filter_by(email=email).first()

        # if user is found, check password is equal to the hash thats stored
        if user:
            # access password
            if check_password_hash(user.password, password):
                flash('Log in successful!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
                flash('Email does not exist.', category='error')
    # boolean attribute can allow if statements in other pages
    return render_template("login.html", boolean=True)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # get info from sign-in form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()


        # validity checks
    
        if user:
            flash('User already exists.', category='error')
        
        # flash message if validity check doesnt pass
        elif len(email) < 4:
            flash('Email must be longer than 4 characters', category='error')
        elif len(first_name) < 2:
            flash('First Name must be longer than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 4:
            flash('Password must be at least 7 characters', category='error')
        else:
            # add user to db
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account Created!', category='success')

            # redirect to homepage after acct creation
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")
