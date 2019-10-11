import flask
from app import app
from flask_socketio import SocketIO, send
from flask_login import current_user

# from flask_login import

# Youtube - Flask + SocketIO
# https://www.youtube.com/watch?v=RdSrkkrj3l4
# pip3 install flask_socketio

#Youtube - Flaks + chat history (no user accounts)
#SQLAlchemy + MySQL (oh well)
#https://www.youtube.com/watch?v=pigpDSOBNMc

socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):  
    print("message:")
    print(msg) 
    print(current_user)

    #This is where I should save it to the DB WITH THE USER NAME
    send(msg, broadcast = True)

#print("mesg:",msg)
 
if __name__ == "__main__":
    #app.run(debug=True)
    socketio.run(app, debug=True)