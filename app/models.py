from app import db, app
from time import strftime
import datetime

class Post(db.Model):
    __tablename__ = 'post'

    # unique ID
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(64), nullable=False)
    writer = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    # relationship
    # comments_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    #작성 시간
    created_time = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        server_default=strftime("%Y-%m-%d %H:%M:%S")
    )
    #최근 수정 시간
    updated_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        server_default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        onupdate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    def __init__(self, title, writer, description):
        self.title = title
        self.writer = writer
        self.description = description

    def __repr__(self):
        return '<Post: {}>'.format(self.id)

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    comment = db.Column(db.String(1024), nullable=False)
    #작성 시간
    created_time = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        server_default=strftime("%Y-%m-%d %H:%M:%S")
    )
    #최근 수정 시간
    updated_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        server_default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        onupdate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    # posts = db.relationship(
    #     'Post',
    #     backref='comment',
    #     lazy='dynamic'
    # )

    def __init__(self, name, email, comment, post_id):
        self.name = name
        self.email = email
        self.comment = comment
        self.post_id = post_id

    def __repr__(self):
        return '<Comment: {}>'.format(self.id)


class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True,
        index=True
    )
    user_name = db.Column(
        db.String(32),
        nullable=False
    )
    korean_name = db.Column(
        db.String(16),
        nullable=False
    )
    email = db.Column(
        db.String(32),
        nullable=False
    )
    password = db.Column(
        db.String(32),
        nullable=False
    )
    colleage = db.Column(
        db.String(32)
    )
    major = db.Column(
        db.String(32)
    )
    student_id = db.Column(
        db.String(32)
    )

    def __init__(selfself, user_name, korean_name, email, password):
        user_name = user_name
        korean_name = korean_name
        password = password
        email = email

    def __repr__(self):
        return '<User: {}>'.format(self.id)
