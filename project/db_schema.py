from config import app
from flask_login import UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True, index = True, nullable = False)
    password = db.Column(db.String(125), unique = False, index = False, nullable = False)
    email = db.Column(db.String(30), unique = True, index = True, nullable = False)
    chatroom_id = db.Column(db.Integer, db.ForeignKey('chatroom.id'))
    messages_sent = db.relationship('Message', backref='sender', lazy='dynamic', cascade='all, delete')


class Chatroom(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    chatroom_id = db.Column(db.Integer, db.ForeignKey('chatroom.id'))
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(150), unique = False, index = True)
    time_sent = db.Column(db.DateTime, unique = False, index = True, default=datetime.utcnow)


