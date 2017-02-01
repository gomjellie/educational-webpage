from flask import render_template, flash, make_response, session,\
        request, url_for, redirect, jsonify
from app import app, db
#from app.forms import RegistrationForm
from app.models import Comment, Post, User
from flask_login import login_user, logout_user, current_user, login_required
from urllib.parse import urlparse, urljoin

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('main/index.html')

@app.route('/board', methods=['GET', 'POST'])
@login_required
def board():
    return render_template('board/index.html')

@app.route('/board/free', methods=['GET', 'POST', 'DELETE'])
@login_required
def board_free():
    posts = Post.query.all()

    # comments = Comment.query.filter_by(posts_id=1).all()
    return render_template('board/free/index.html',
                           posts=posts
                           )

@app.route('/board/free/<int:post_id>', methods=['GET', 'POST'])
def board_free_id(post_id):
    if request.method == 'POST':
        comment = Comment(
            name=request.form.get('name'),
            email=request.form.get('email'),
            comment=request.form.get('comment'),
            post_id=post_id
        )
        db.session.add(comment)
        db.session.commit()
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post.id).all()
    return render_template('board/free/post/index.html',
                           post=post,
                           comments=comments
                           )

@app.route('/board/free/delete_comment/<int:comment_id>', methods=['REMOVE', 'GET'])
def board_free_delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(request.referrer)

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

@app.route('/account/login_required', methods=['GET', 'POST'])
def login_required():
    return render_template('account/login-required/index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        user = User(
            username=request.form.get('username'),
            password=request.form.get('password'),
            email=request.form.get('email')
        )

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember')
        json_res = {
            'user_id': username,
            'password': password,
            'remember': remember
        }
        print(str(request.form))
        print(json_res)
        user = User.query.filter_by(username=username).first()
        if not user:
            print(username + " doesn't exists")
            json_res = {
                'ok': False,
                'message': 'Invalid user_id'
            }
        elif user.password != password:
            print("password: " + password + " is wrong!")
            json_res = {
                'ok': False,
                'message': 'Invalide password'
            }
        else:
            print("login success")
            user.authenticated = True
            login_user(user=user, remember=remember)

    next_url = request.args.get('next')
    return redirect(
        next_url or request.referrer)

@app.route('/api/login', methods=["GET", "POST"])
def api_login():
    if request.method == 'POST':
        username = request.json['user_id']  # form['username']
        password = request.json['password']  # form['password']
        user = User.query.filter_by(username=username).first()
        if not user:
            json_res = {
                'ok': False,
                'message': 'Invalid user_id'
            }
        elif user.password != password:
            json_res = {
                'ok': False,
                'message': 'Invalide password'
            }
        else:
            login_user(user=user, remember=True)
            json_res = {
                'ok': True,
                'message': str(username) + ' log in success'
            }
        return jsonify(json_res)

@app.errorhandler(404)
def non_existant_route(error):
    return jsonify({
        "no": "such page"
    })

# @app.teardown_request
# def shutdown_session(exception=None):
#     db.session().remove()
