from app import db
from time import strftime

class Post(db.Model):
    def __init__(self, title, writer, description):
        self.title = title
        self.writer = writer
        self.description = description

    # unique ID
    id = db.Column(
        db.Integer,
        primary_key=True,
        index=True
    )
    # 제목
    title = db.Column(
        db.String(64),
        nullable=False
    )
    # 게시자
    writer = db.Column(
        db.String(32),
        nullable=False
    )
    # 작성 시간
    # created_time = db.Column(
    #     db.DateTime,
    #     server_default=strftime("%m-%d-%Y %H:%M:%S")
    # )
    # 최근 수정 시간
    # updated_time = db.Column(
    #     db.DateTime,
    #     server_default=strftime("%m-%d-%Y %H:%M:%S"),
    #     onupdate=strftime("%m-%d-%Y %H:%M:%S")
    # )
    # 내용
    description = db.Column(
        db.String(255),
        nullable=False
    )

class Comment(db.Model):
    def __init__(self, name, email, comment):
        self.name = name
        self.email = email
        self.comment = comment

    id = db.Column(
        db.Integer,
        primary_key=True,
        index=True
    )

    name = db.Column(
        db.String(32),
        nullable=False
    )

    email = db.Column(
        db.String(32),
        nullable=False
    )

    comment = db.Column(
        db.String(1024),
        nullable=False
    )

