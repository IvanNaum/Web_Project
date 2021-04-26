from flask import render_template
from flask_login import current_user
from flask_socketio import emit

import constants
from components import socket, app, sessions, User
from components.checkers.session import Session


def find_session(user):
    sess = list(filter(lambda x: user in x.get_users(), sessions))
    if sess:
        return sess[0]


def find_none_session():
    none_sess = list(filter(lambda x: None in x.get_users(), sessions))
    if none_sess:
        return none_sess[0]


@socket.on('data')
def get_data():
    if not current_user.is_authenticated:
        return

    sess = find_session(current_user)
    if sess.user2:
        board, color = sess.get_pieces(current_user)
        emit('data', {'board': board,
                      'user_color': color,
                      'black': constants.BLACK,
                      'white': constants.WHITE})
    else:
        emit('data', {'message': 'Противник ещё не найден'})


@socket.on('step')
def step(data):
    if find_session(current_user):
        from_x, from_y = data['from_x'], data['from_y']
        to_x, to_y = data['to_x'], data['to_y']

        ...


@app.route('/game')
def game_page():
    if not current_user.is_authenticated:
        return

    sess = find_session(current_user)
    if sess and sess.user1 == current_user:
        sessions.remove(sess)
        sess = None

    # Если существует комната с пользователем, возвращаем её
    if not sess:
        # Если есть комната с одним человеком, добавляем текущего юзера
        none_sess = find_none_session()
        if none_sess:
            none_sess.set_user2(User.query.filter_by(id=current_user.id).first())
        else:
            # Если нет, создаем новую комнату
            sessions.append(Session(User.query.filter_by(id=current_user.id).first()))
        sess = find_session(current_user)

    board, user_color = sess.get_data_by_user(current_user)
    return render_template('game.html', current_user=current_user, board=board,
                           user_color=user_color, WHITE=constants.WHITE)
