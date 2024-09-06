#12. Build a Flask app that updates data in real-time using WebSocket connections.

from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Function to emit real-time data
def update_data():
    while True:
        time.sleep(5)  # Simulate data updates every 5 seconds
        # Emit updated data to all connected clients
        socketio.emit('update_data', {'value': time.time()})

# Background thread to simulate real-time data updates
@socketio.on('connect')
def handle_connect():
    print("Client connected")
    # Start the data update thread
    threading.Thread(target=update_data).start()

if __name__ == '__main__':
    socketio.run(app, debug=True)