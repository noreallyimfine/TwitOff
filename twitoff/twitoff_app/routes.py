from flask import render_template
from twitoff_app import app, DB


# route determines location
@app.route('/')
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')
