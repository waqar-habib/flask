# 
from flask import Blueprint, render_template

# define "views.py" as blueprint of app
views = Blueprint('views', __name__)

# define initial route using decorator
@views.route('/')
def home():
    return render_template ("home.html")