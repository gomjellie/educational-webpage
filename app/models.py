from app import db, app
from time import strftime
import datetime
from flask_login import LoginManager, login_required, login_user, \
    logout_user, UserMixin

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
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password = db.Column(db.String(10))
    email = db.Column(db.String(50), unique=True, index=True)
    registered_on = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
        server_default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        onupdate=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    # 단과대학 ex) 경영대학, it대학, 공과대학
    colleage = db.Column(db.String(32))
    major = db.Column(db.String(32))
    # 학번 ex) 20150318
    student_id = db.Column(db.String(32), unique=True)
    phone_number = db.Column(db.String(16))
    new_info = db.Column(db.String(16))

    def __init__(self, username, password, email,
                 major, student_id, phone_number,
                 new_info,
                 authenticated=False):
        self.username = username
        self.password = password
        self.email = email
        self.major = major
        self.student_id = student_id
        self.phone_number = phone_number
        self.authenticated = authenticated
        self.new_info = new_info

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id  # unicode(self.id)

    def can_login(self, password):
        return self.password == password

    def __repr__(self):
        return '<User %r>' % self.username
