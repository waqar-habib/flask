# 
from flask import Blueprint

# define "views.py" as blueprint of app
views = Blueprint('views', __name__)

# define initial route using decorator
@views.route('/')
def home():
    return "<h1>Test</h1>"