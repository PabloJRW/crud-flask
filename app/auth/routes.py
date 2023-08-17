from flask import render_template, current_app
from . import auth_bp


@auth_bp.route("/login")
def login():
    return render_template('auth/login.html')


@auth_bp.route("/signup")
def signup():
    return render_template('auth/signup.html')
