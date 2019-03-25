from datetime import datetime

from blog import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    picture = db.Column(db.String(64), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return 'User({}, {})'.format(self.username, self.email)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date_posted = db.DateTime(default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return 'Post({}, {})'.format(self.title, self.date_posted)
