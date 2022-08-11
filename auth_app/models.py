# create db models

# importing db object from current package
from . import db
# custom class can be inherited, gives user info for login
from flask_login import UserMixin

# create user model
class User(db.Model, UserMixin):
    # define schema for db
    id = db.Column(db.Integer, primary_key=True) # set up primary key, int. represents object
    email = db.Column(db.String(150) unique=True) #pass in length allowed
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))