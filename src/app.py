import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length

from database import SessionLocal
from sqlalchemy.orm import Session


template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')


app = Flask(__name__, template_folder=template_dir)
app.config.from_mapping(
    SECRET_KEY = 'dev'
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from productos import productos
productos = productos

# Rutas de la aplicación 
@app.route('/', methods=['GET', 'POST'])
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


@app.route('/registro')
def registro():
    return render_template('registro.html', productos=productos)


class SignUpForm(FlaskForm):
    username = StringField("Nombre de Usuario: ", validators=[DataRequired(), Length(min=4, max=12)])
    email = EmailField("Correo Electrónico: ", validators=[DataRequired()])
    password = PasswordField(" Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
    password2 = PasswordField("Confirma la Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
    submit = SubmitField("Registrar")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data

        return f"{username}, {email}"

    return render_template('auth/register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5050)


#