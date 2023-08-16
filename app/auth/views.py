from flask import render_template, current_app
from . import auth_bp
import os

@auth_bp.route("/")
@auth_bp.route("/user-registration")
def register():
    template_name = "auth/user-registration.html"
    template_path = os.path.join(current_app.template_folder, template_name)
    print("Template path:", template_path)
    return render_template(template_name)


@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")


@auth_bp.route("/signup")
def signup():
    return render_template("auth/signup.html")
