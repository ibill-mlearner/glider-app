
from flask_socketio import SocketIO, emit

socketio = SocketIO()

def init_socketio(app):
    socketio.init_app(app)

    @socketio.on('connect')
    def handle_connect():
        emit('status', {'msg': 'Connected to glider engine'})

    @socketio.on('request_state')
    def handle_state_request():
        # Replace with real simulation state
        emit('state_update', {'gliders': []})