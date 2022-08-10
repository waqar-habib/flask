from flask import Blueprint, render_template

# define "auth.py" as blueprint of app
auth = Blueprint('auth', __name__)

#define login, logout, sign up using render_template
#ln 12: can pass in variable as a 2nd argument in render_template function, use it in any other page

@auth.route('/login')
def login():
    # boolean attribute can allow if statements in other pages
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def signup():
    return render_template("sign_up.html")