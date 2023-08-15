import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length

#from database import SessionLocal
#from sqlalchemy.orm import Session

from productos import productos


def create_app():
    template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    template_dir = os.path.join(template_dir, 'src', 'templates')


    app = Flask(__name__, template_folder=template_dir)
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY = 'dev'
    )
    

    class RegistrarForm(FlaskForm):
        id_ = StringField("Id del Producto")
        nombre = StringField("Producto")
        proveedor = StringField("Proveedor")
        categoria = StringField("Categoría")
        lote = StringField("Lote")
        cantidad = StringField("Cantidad")
        descripcion = StringField("Descripción")
        submit = SubmitField("Guardar")

    # Rutas de la aplicación 
    @app.route('/registrar', methods=['GET', 'POST'])
    def home():
        form = RegistrarForm()
        if form.validate_on_submit():
            id_ = form.id_.data
            nombre = form.nombre.data
            proveedor = form.proveedor.data
            categoria = form.categoria.data
            lote = form.lote.data
            cantidad = form.cantidad.data
            descripcion = form.descripcion.data

            f"{id_}, {nombre}, {proveedor}"
        
        return render_template('index.html')

    @app.route('/')
    @app.route('/registros')
    def registros():
        return render_template('registro.html', productos=productos)


    class SignUpForm(FlaskForm):
        username = StringField("Nombre de Usuario: ", validators=[DataRequired(), Length(min=4, max=12)])
        email = EmailField("Correo Electrónico: ", validators=[DataRequired()])
        password = PasswordField(" Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
        password2 = PasswordField("Confirma la Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
        submit = SubmitField("Sign up")


    @app.route('/signup', methods=['GET', 'POST'])
    def register():
        form = SignUpForm()
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            password2 = form.password2.data

            return f"{username}, {email}"

        return render_template('auth/signup.html', form=form)


    return app




#