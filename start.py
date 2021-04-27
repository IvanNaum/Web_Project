import os

from components import app, socket

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socket.run(app=app, port=8000)
