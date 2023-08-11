import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
#import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')


app = Flask(__name__, template_folder=template_dir)


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

        producto= {'id':id_, 'nombre': nombre, 'proveedor':proveedor, 'categoria':categoria, 'lote':lote, 'cantidad':cantidad, 'descripcion':descripcion}

    
    return render_template('index.html')


@app.route('/registro')
def registro():
    return render_template('registro.html', productos=productos)


class RegisterForm(FlaskForm):
    username = StringField("Nombre de Usuario: ")
    password = PasswordField(" Contraseña: ")
    email = EmailField("Correo Electrónico: ")
    repeatPassword = PasswordField("Confirma la Contraseña: ")


@app.route('/register')
def register():
    form = RegisterForm
    return render_template('auth/register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5050)


#