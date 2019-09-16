"""Entry point for TwitOff"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitoff.db'
DB = SQLAlchemy(app)

from twitoff_app import routes
