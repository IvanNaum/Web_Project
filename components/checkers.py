from flask import render_template

from components import socket, app


@socket.on('my event')
def test(data):
    print('тест', data)


@app.route('/game')
def game_page():
    return render_template('game.html')
