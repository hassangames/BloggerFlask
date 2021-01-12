from flask import Blueprint
mainView = Blueprint("/mainView", __name__)
from . import views
