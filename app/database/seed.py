from app import db
from app.models import Post, Comment

def create_posts():
    post1 = Post("title1", "writer1", "description1")
    post2 = Post("title2", "writer2", "description2")
    #comment1 = Comment("comment's name1", "comment's email1", "comment1's contents")
    #comment2 = Comment("comment's name2", "comment's email2", "comment2's contents")

    # post1.comments = comment1  # [comment1, comment2]
    # post1.comments.append(comment2)
    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()

def create_comment():
    for i in range(1, 3):
        comment1 = Comment("name" + str(i), "email" + str(i), "comment" + str(i), i)
        db.session.add(comment1)

    db.session.commit()

def run_seed():
    create_posts()
    create_comment()
