from datetime import datetime
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
# from . import db
db = SQLAlchemy()
# db.init_app(current_app)
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

from flask_login import UserMixin


class user(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    enabled = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_publisher = db.Column(db.Boolean, default=False)
    posts = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return "{},{}".format(self.id, self.fname)


class post(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    author = db.relationship('user', backref="post.id")


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))



