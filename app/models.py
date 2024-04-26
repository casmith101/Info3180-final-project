from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(100))
    biography = db.Column(db.Text)
    profile_photo = db.Column(db.String(100))
    joined_on = db.Column(db.DateTime)

    def __init__(self, username, password, firstname, lastname, email, location, biography, profile_photo):
        self.username = username
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', password_hash='{self.password_hash}', firstname='{self.firstname}', lastname='{self.lastname}', email='{self.email}', location='{self.location}', biography='{self.biography}', profile_photo={self.profile_photo}, joined_on={self.joined_on})"


    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', password_hash='{self.password_hash}', firstname='{self.firstname}', lastname='{self.lastname}', email='{self.email}', location='{self.location}', biography='{self.biography}', profile_photo={self.profile_photo}, joined_on={self.joined_on})"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(255))
    photo = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

if __name__ == '__main__':
    db.create_all()
