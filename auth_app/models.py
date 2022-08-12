# create db models

# importing db object from current package
from time import timezone
from . import db
# custom class can be inherited, gives user info for login
from flask_login import UserMixin
from sqlalchemy.sql import func

# create user model
class User(db.Model, UserMixin):
    # define schema for db
    id = db.Column(db.Integer, primary_key=True) # set up primary key, int. represents object
    email = db.Column(db.String(150), unique=True) #pass in length allowed
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #add this note into user's id

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #func gets current date/time
    
    #create relationship b/w note and user using foreign key. Must pass valid id of existing user. one to many relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #primary key of the obj used