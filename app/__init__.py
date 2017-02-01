from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import urandom
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY=urandom(24),
    USERNAME='admin',
    PASSWORD='default',
    static_folder='static',
    template_folder='templates',
    static_url_path = "templates",
    SQLALCHEMY_DATABASE_URI='sqlite:///educational.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ))

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_required"
login_manager.login_message = "this is login message"

from app import models
from app import views

from app.helpers.jinja import regex_replace
from app.helpers.login import user_loader
