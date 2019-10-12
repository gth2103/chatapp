import flask
import time
from app import app
from flask import request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_login import current_user
from flask_socketio import ConnectionRefusedError

# from flask_login import

# Youtube - Flask + SocketIO
# https://www.youtube.com/watch?v=RdSrkkrj3l4
# pip3 install flask_socketio

#Youtube - Flaks + chat history (no user accounts)
#SQLAlchemy + MySQL (oh well)
#https://www.youtube.com/watch?v=pigpDSOBNMc

socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(data): 
	print(request.sid)
	print("message:")
	print(data)
	print(current_user)

	#This is where I should save it to the DB WITH THE USER NAME

	#send(msg, broadcast = True)
	send({'msg': data['msg'], 'user': data['user'], 'time': time.strftime('%b %d %I:%M%p', time.localtime()), 'room': data['room']}, room = data['room'])

@socketio.on('join')
def join(data):

	join_room(data['room'])
	send({'msg': data['user'] + " has joined the room.", 'user': data['room'], 'time': time.strftime('%b %d %I:%M%p', time.localtime())}, room = data['room'])

@socketio.on('leave')
def leave(data):

	leave_room(data['room'])
	send({'msg': data['user'] + " has left the room.", 'user': data['room'], 'time': time.strftime('%b %d %I:%M%p', time.localtime())}, room = data['room'])
#@socketio.on('image')
#def handleImage(img):
#	print("image: ")
#	print(img)
#	file = open(img, 'rb')
#	image_bin = file.read()
#	emit('image', { image_bin: image_bin}, broadcast = True);

@socketio.on('disconnect')
def test_disconnect():
	print('Client disconnected')

@socketio.on('connect')
def connect_handler():
    if current_user.is_authenticated:
        emit('my response',
             {'message': '{0} has joined'.format(current_user.username)})
    else:
        return False  # not allowed here

 
if __name__ == "__main__":
    #app.run(debug=True)
    socketio.run(app, debug=True)