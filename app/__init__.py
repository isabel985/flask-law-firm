from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging, os
from logging.handlers import SMTPHandler, RotatingFileHandler

app = Flask(__name__, static_folder='static')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config.from_object(Config)

from app import routes, models