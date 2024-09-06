// Establish WebSocket connection
var socket = io.connect('http://' + document.domain + ':' + location.port);

// Listen for 'notification' events from the server
socket.on('notification', function(data) {
    var notificationContainer = document.getElementById('notification-container');
    var notificationElement = document.createElement('div');
    notificationElement.className = 'notification';
    notificationElement.textContent = data.message;
    notificationContainer.appendChild(notificationElement);
});