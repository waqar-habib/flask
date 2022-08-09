from flask import Flask

# create basic app
def create_app():
    app = Flask(__name__)
    #encrypt session data
    app.config['SECRET_KEY'] = 'kefnkwelk ewklfnefk'

    return app

