import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length

from flask_sqlalchemy import SQLAlchemy
#from database import SessionLocal
#from sqlalchemy.orm import Session

from productos import productos

db = SQLAlchemy()



template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')


app_bp = Flask(__name__, template_folder=template_dir)
app_bp.config.from_mapping(
    DEBUG=True,
    SECRET_KEY = 'dev',
    SQLALCHEMY_DATABASE_URI = "sqlite:///projects.db"
)


db.init_app(app_bp)


# Rutas de la aplicación 
@app_bp.route('/registrar', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        id_ = request.form['idProducto']
        nombre = request.form['nombreProducto']
        proveedor = request.form['proveedorProducto']
        categoria = request.form['categoriaProducto']
        lote = request.form['loteProducto']
        cantidad = request.form['cantidadProducto']
        descripcion = request.form['descripcionProducto']

        producto= [id_, nombre, proveedor, categoria, lote, cantidad, descripcion]
    # db.add(producto)
    
    return render_template('index.html')

@app_bp.route("/")
@app_bp.route('/registro')
def registro():
    return render_template('registro.html', productos=productos)


class SignUpForm(FlaskForm):
    username = StringField("Nombre de Usuario: ", validators=[DataRequired(), Length(min=4, max=12)])
    email = EmailField("Correo Electrónico: ", validators=[DataRequired()])
    password = PasswordField(" Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
    password2 = PasswordField("Confirma la Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
    submit = SubmitField("Sign up")


@app_bp.route('/signup', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data

        return f"{username}, {email}"

    return render_template('auth/signup.html', form=form)


with app_bp.app_context():
    db.create_all()

