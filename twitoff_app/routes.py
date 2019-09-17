from flask import render_template
from twitoff_app import app, DB
from .models import User


# route determines location
@app.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)


@app.route("/about")
def about():
    return render_template('about.html')
