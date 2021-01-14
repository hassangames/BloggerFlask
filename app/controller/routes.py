from . import controller_
from flask import request, render_template
from app.models import user, db
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf import FlaskForm


@controller_.route("/signup", methods=['GET', 'POST'])
def signup():
    print(request.form)
    print(request.headers)
    if request.method == 'POST':
        email = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        password = request.form['password']
        if all([email, fname, lname, password]):
            user_data = user(email=email, fname=fname, lname=lname, password=password)
            db.session.add(user_data)
            db.session.commit()
            db.session.close()
            return "Saved!"
        else:
            return "Missing Data"
    else:
        return render_template('signup.html')
