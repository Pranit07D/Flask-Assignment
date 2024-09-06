#13. Implement notifications in a Flask app using websockets to notify users of updates.

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

# Route for the notifications page
@app.route('/')
def index():
    return render_template('index.html')

# Function to simulate sending notifications
def send_notifications():
    count = 0
    while True:
        time.sleep(10)  # Simulate a notification every 10 seconds
        count += 1
        # Create a notification message
        message = f"Notification #{count}"
        # Emit the notification to all connected clients
        socketio.emit('notification', {'message': message})

# Handle client connections
@socketio.on('connect')
def handle_connect():
    print("Client connected")
    # Start the notification thread
    threading.Thread(target=send_notifications).start()

if __name__ == '__main__':
    socketio.run(app, debug=True)