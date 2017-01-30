from flask import render_template, flash, make_response, session,\
        request, url_for, redirect
from app import app, db
#from app.forms import RegistrationForm
from app.models import Comment, Post

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('base/index.html')

@app.route('/board', methods=['GET', 'POST'])
def board():
    return render_template('board/index.html')

@app.route('/board/free', methods=['GET', 'POST', 'DELETE'])
def board_free():
    if request.method == 'POST':
        comment = Comment(
            request.form.get('name'),
            request.form.get('email'),
            request.form.get('comment')
        )
        db.session.add(comment)
        db.session.commit()
    posts = Post.query.all()
    comments = Comment.query.all()
    return render_template('board/free/index.html',
                           posts=posts,
                           comments=comments
                           )

@app.route('/board/free/delete_comment/<int:comment_id>', methods=['REMOVE', 'GET'])
def board_free_delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('board_free'))

@app.route('/style_demo', methods=['GET', 'POST', 'DELETE'])
def style_demo():
    if request.method == 'POST':
        comment = Comment(
            request.form.get('name'),
            request.form.get('email'),
            request.form.get('comment'),
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(request.url)
    comments = Comment.query.all()

    return render_template('style-demo/index.html', comments=comments)

@app.route('/style_demo/delete_comment/<int:comment_id>', methods=['REMOVE', 'GET'])
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('style_demo'))

@app.route('/account/new', methods=['GET', 'POST'])
def new_account():
    return render_template('account/new/index.html')
