from application.main import socketio
from application.main import app
if __name__ == "__main__":
        socketio.run(app,host='127.0.0.1', debug=True)