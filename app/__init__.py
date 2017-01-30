from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    static_folder='static',
    template_folder='templates',
    static_url_path = "templates",
    SQLALCHEMY_DATABASE_URI='sqlite:///educational.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ))

db = SQLAlchemy(app)

from app import models
from app import views

from app.helpers.jinja import regex_replace