from flask import *
from flask_sqlalchemy import SQLAlchemy

from .auth import auth as authRouter
from .main import mainView

db = SQLAlchemy()


def Create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.register_blueprint(authRouter, url_prefix=str("/auth"))
    app.register_blueprint(mainView, url_prefix=str("/"))
    return app # the actual flask app
