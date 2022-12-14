from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user, item
from flask_app.controllers import items

@app.route('/register', methods=["POST"])
def create_user():
    if user.User.create_user(request.form):
        return redirect ('/dashboard')
    else:
        return redirect('/')

@app.route('/')
def login_page():
    return render_template("login.html")

@app.route('/user/login', methods=["POST"])
def login_user():
    if user.User.login_user(request.form):
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/user/logout')
def logout_user():
    session.clear()
    return redirect('/')