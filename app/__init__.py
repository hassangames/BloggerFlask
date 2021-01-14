from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app_config import Config
from .auth import auth as authRouter
from .main import mainView
from .controller import controller_
db = SQLAlchemy()


def Create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(authRouter, url_prefix=str("/auth"))
    app.register_blueprint(mainView, url_prefix=str("/"))
    app.register_blueprint(controller_, url_prefix=str("/c"))
    return app # the actual flask app
