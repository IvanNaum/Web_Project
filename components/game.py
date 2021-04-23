from flask import render_template
from flask_login import current_user
from flask_socketio import emit

import constants
from components import socket, app, sessions


@socket.on('pieces')
def get_pieces():
    sess = list(filter(lambda x: current_user in x.get_users(), sessions))[0]

    board, color = sess.get_peaces(current_user)
    emit('pieces', {'board': board,
                    'user_color': color,
                    'black': constants.BLACK,
                    'white': constants.WHITE})


@app.route('/game')
def game_page():
    sess = list(filter(lambda x: current_user in x.get_users(), sessions))[0]
    board, user_color = sess.get_data_by_user(current_user)
    return render_template('game.html', current_user=current_user, board=board,
                           user_color=user_color, WHITE=constants.WHITE)
