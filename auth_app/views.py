# 
from flask import Blueprint, render_template
from flask_login import login_required, current_user

# define "views.py" as blueprint of app
views = Blueprint('views', __name__)

# define initial route using decorator
@views.route('/')
@login_required
def home():
    # reference in home if current user is authenticated
    return render_template ("home.html", user=current_user)