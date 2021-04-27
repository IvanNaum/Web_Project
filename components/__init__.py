from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from components.checkers.session import Session

app = Flask(__name__)
app.debug = True

app.secret_key = 'secret string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

socket = SocketIO(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from components import models

db.create_all()

from components.models import User

# Список с информацией о игровых комнатах
sessions = []

from components import main_page, authorization, game
