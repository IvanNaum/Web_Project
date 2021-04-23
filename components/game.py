from flask import render_template
from flask_login import current_user

import constants
from components import socket, app, sessions


@socket.on('my event')
def test(data):
    print('тест', data)


@app.route('/game')
def game_page():
    user = current_user
    sess = list(filter(lambda x: user in x.get_users(), sessions))[0]
    board, user_color = sess.get_data_by_user(user)
    return render_template('game.html', current_user=user, board=board, user_color=user_color, WHITE=constants.WHITE)
