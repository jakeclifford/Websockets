from flask import Flask, render_template, make_response, redirect
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

#hhj
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on("message")
def handleMessage(data):
    emit("new_message",data,broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5004)
