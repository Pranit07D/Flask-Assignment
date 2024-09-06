// Establish connection to WebSocket server
var socket = io.connect('http://' + document.domain + ':' + location.port);

// Event listener for receiving messages
socket.on('message', function(msg) {
    var chatBox = document.getElementById('chat-box');
    var messageElement = document.createElement('p');
    messageElement.innerHTML = msg;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;  // Auto-scroll to the bottom
});

// Function to send a message when "Send" button is clicked
function sendMessage() {
    var messageInput = document.getElementById('message');
    var message = messageInput.value;
    if (message.trim() !== "") {
        socket.send(message);
        messageInput.value = '';  // Clear input field after sending
    }
}