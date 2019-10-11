

from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from flask_socketio import SocketIO, send



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

socketio = SocketIO(app)

# login_manager.init_app(app)

login = LoginManager(app)
login.init_app(app)

from app import routes, models



