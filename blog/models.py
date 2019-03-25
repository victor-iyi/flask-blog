from datetime import datetime

from blog import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'User({self.username}, {self.email})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Text(nullable=False)
    date_posted = db.DateTime(default=datetime.utcnow)

    def __repr__(self):
        return f'Post({self.title})'
