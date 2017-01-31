from flask import render_template, flash, make_response, session,\
        request, url_for, redirect, jsonify
from app import app
from app.models import User
from flask_login import login_user, logout_user, current_user

@app.route('/api/login', methods=["GET", "POST"])
def login():
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
            user.authenticated = True
            login_user(user=user, remember=True)
            json_res = {
                'ok': True,
                'message': str(username) + 'log in success'
            }
        return jsonify(json_res)
