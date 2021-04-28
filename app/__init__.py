from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

socket = SocketIO(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

sessions = []

from app import models, auth, main

db.create_all()
