from flask import Flask

# create basic app
def create_app():
    app = Flask(__name__)
    #encrypt session data
    app.config['SECRET_KEY'] = 'kefnkwelk ewklfnefk'

    # import blueprints
    from .views import views
    from. auth import auth

    # doing this to access routes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app

