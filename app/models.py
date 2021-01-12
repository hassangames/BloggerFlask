from datetime import datetime

from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


class user(db.Model, UserMixin):
    id = db.Column()
    email = db.Column()
    fname = db.Column()
    lname = db.Column()
    password = db.Column()
    enabled = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_publisher = db.Column(db.Boolean, default=False)
    posts = db.Column(db.Integer,db.ForeignKey('Blogger.user'))