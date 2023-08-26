from flask import render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth_bp
from .forms import SignUpForm, LoginForm 
from app.models.models import User
from app import db


# Endpoint para el registro de usuarios nuevos
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data

        # Verifica si el usuario ya existe en la base de datos
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('El nombre del usuario ya está en uso.', 'danger')
            return redirect(url_for('auth.signup'))
        
        # Crea un nuevo objeto User y lo agrega a la base de datos
        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        print(new_user.id)

        flash('Registro exitoso. ¡Ahora puedes iniciar sesión', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', form=form)


# # Endpoint para el inicio de sesión de usuarios existentes
@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        username_or_email = loginform.username_or_email.data
        password = loginform.password.data

        existing_user = User.query.filter_by(username=username_or_email).first()
        if existing_user:
            if check_password_hash(existing_user.password, password):
                session.clear()
                session['user_id'] = existing_user.id
                flash('Sesión iniciada!.')
                return redirect(url_for('main.registros'))
            
        else:
            flash('Usuario o contraseña incorrecta!.', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html', loginform=loginform)


