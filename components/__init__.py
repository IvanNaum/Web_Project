from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from components.checkers.board import Board

app = Flask(__name__)
app.secret_key = 'secret string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

socket = SocketIO(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Список словарей с информацией о игровых комнатах
sessions = [
    {
        'user1': 1,
        'user2': 3,
        'board': Board()
    }
]

from components import main_page, models, authorization, game
