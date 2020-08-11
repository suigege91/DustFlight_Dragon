import sys

sys.path.append("../")
from main import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(128))
    user_pass = db.Column(db.String(128))
    user_male = db.Column(db.String(9))
    user_mail = db.Column(db.String(128))
    user_address = db.Column(db.String(128))
    user_register_date = db.Column(db.DateTime, default=datetime.now)
    user_last_logon_date = db.Column(db.DateTime, default=datetime.now)
    user_posts = db.relationship('Post', backref='users', lazy='dynamic')

    def __init__(self, user_name, user_pass, user_male, user_mail, user_address):
        self.user_name = user_name
        self.user_pass = user_pass
        self.user_male = user_male
        self.user_mail = user_mail
        self.user_address = user_address

    def __repr__(self):
        return "<User `{}`>".format(self.user_name)


class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    post_title = db.Column(db.String(255))
    post_content = db.Column(db.Text())
    post_publish_date = db.Column(db.DateTime, default=datetime.now)
    post_modify_date = db.Column(db.DateTime, default=datetime.now)
    post_user_id = db.Column(db.Integer(), db.ForeignKey('users.user_id'))

    def __init__(self, post_title, post_content):
        self.post_title = post_title
        self.post_content = post_content

    def __repr__(self):
        return "<Post `{}`>".format(self.post_title)
