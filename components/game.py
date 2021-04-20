from flask import render_template
from flask_login import current_user

from components import socket, app, sessions


@socket.on('my event')
def test(data):
    print('тест', data)


@app.route('/game')
def game_page():
    sess = list(filter(lambda x: x['user1'] == current_user.id, sessions))[0]
    board = sess['board']
    return render_template('game.html', current_user=current_user, board=board)
