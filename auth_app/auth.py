from flask import Blueprint, render_template, request

# define "auth.py" as blueprint of app
auth = Blueprint('auth', __name__)

#define login, logout, sign up using render_template
#can pass in variable as a 2nd argument in render_template function, use it in any other page

# The route below can accept get and post methods
@auth.route('/login', methods=['GET', 'POST'])

def login():

    # has all data that was sent as a part of this form
    data = request.form

    # prints immutable dict with info that was filled out in the form
    print(data)
    
    # boolean attribute can allow if statements in other pages
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    return render_template("sign_up.html")