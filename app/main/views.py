from flask import *
from . import mainView


@mainView.route('/')
def Index():
    return "<h1>Index Page :)</h1>"


