from app import app, socket

socket.run(app=app, host='127.0.0.1', port=8000)
