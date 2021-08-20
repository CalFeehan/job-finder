from flask import Flask
from flask_session import Session
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    app.config['SESSION_PERMANENT'] = True
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)
    app.config['SESSION_FILE_THRESHOLD'] = 50

    app.config['SECRET_KEY'] = 'changelater'

    Session(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
