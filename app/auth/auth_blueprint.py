from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length
from . import auth_bp
from app.models.models import User


@auth_bp.route("/user-registration")
def signup():
    return render_template('auth/user-registration.html')


@auth_bp.route("/login")
def login():
    return render_template('auth/login.html')


class SignUpForm(FlaskForm):
    username = StringField("Nombre de Usuario: ", validators=[DataRequired(), Length(min=4, max=12)])
    email = EmailField("Correo Electrónico: ", validators=[DataRequired()])
    password = PasswordField(" Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
    password2 = PasswordField("Confirma la Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
    submit = SubmitField("Sign up")


@auth_bp.route('/signup', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data

        return f"{username}, {email}"

    return render_template('auth/signup.html', form=form)