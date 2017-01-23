from app import db
from app.models import Post, Comment

def create_posts():
    post1 = Post("title1", "writer1", "description1")
    db.session.add(post1)
    db.session.commit()

def create_comment():
    comment1 = Comment("name1", "email1", "comment1")
    db.session.add(comment1)
    db.session.commit()

def run_seed():
    create_posts()
    create_comment()
