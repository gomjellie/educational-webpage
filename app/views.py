from flask import render_template, flash, make_response, session,\
        request, url_for, redirect
from app import app, db
#from app.forms import RegistrationForm
from app.models import Comment

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('base/index.html')

@app.route('/board', methods=['GET', 'POST'])
def board():
    return render_template('board/index.html')

@app.route('/style_demo', methods=['GET', 'POST'])
def style_demo():
    if request.method == 'POST':
        comment = Comment(
            request.form.get('name'),
            request.form.get('email'),
            request.form.get('comment'),
        )
        db.session.add(comment)
        db.session.commit()
    comments = Comment.query.all()

    return render_template('style-demo/index.html', comments=comments)
