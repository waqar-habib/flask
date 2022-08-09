from flask import Blueprint

# define "auth.py" as blueprint of app
auth = Blueprint('auth', __name__)

#define login, logout, sign up

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def signup():
    return "<p>Sign-Up</p>"