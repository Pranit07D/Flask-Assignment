var socket = io.connect('http://' + document.domain + ':' + location.port);

// Listen for the 'update_data' event from the server
socket.on('update_data', function(data) {
    document.getElementById('data').innerHTML = 'Updated Value: ' + data.value;
});