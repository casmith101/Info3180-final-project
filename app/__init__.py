from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
# import flask migrate here

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate= Migrate(app, db)
# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views
