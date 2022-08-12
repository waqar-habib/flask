from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# define new db. This is a database object
db = SQLAlchemy()
DB_NAME= "database.db"

# create basic app
def create_app():
    app = Flask(__name__)
    #encrypt session data
    app.config['SECRET_KEY'] = 'kefnkwelk ewklfnefk'
    # sql alchemy db is located below in db_name. Store db is flask folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    #initialize db
    db.init_app(app)



    # import blueprints
    from .views import views
    from. auth import auth

    # doing this to access routes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # defines class User and Notes to create db. Mind the relative import strategy
    from .models import User, Note

    # initialize function
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('flask/' + DB_NAME):
        db.create_all(app=app)
        print('Database created!')



