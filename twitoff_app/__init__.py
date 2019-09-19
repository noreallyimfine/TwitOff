"""Entry point for TwitOff"""
from decouple import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['ENV'] = config('ENV')
DB = SQLAlchemy(app)

from twitoff_app import routes
