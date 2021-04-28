from components import app, socket

socket.run(app=app, host='0.0.0.0', port=5000)
