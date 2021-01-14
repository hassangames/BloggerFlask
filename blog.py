from app import Create_app, db
from app.models import db as db_test,user

app = Create_app()
with app.app_context():
    db_test.init_app(app)
    db_test.create_all()

