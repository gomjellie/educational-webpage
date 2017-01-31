from flask import Flask, Response, session
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, login_required, login_user,\
    logout_user, UserMixin

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY=os.urandom(24),
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

from app import models
from app import views

from app.helpers.jinja import regex_replace
from app.helpers.login import user_loader
