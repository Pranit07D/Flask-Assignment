#11. Create a real-time chat application using Flask-SocketIO.

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Route for the chat page
@app.route('/')
def chat():
    return render_template('chat.html')

# Handle incoming messages from clients
@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    # Broadcast the message to all clients
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)