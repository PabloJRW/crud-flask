from flask import render_template, request
from app.main import  main_bp
from app.models.models import Registro
from productos import productos
from app import db
import csv
from io import StringIO


@main_bp.route('/registros')
def registros():
    inventario = db.session.query(Registro).all()
    return render_template('main/registro.html', productos=inventario) 


# Rutas de la aplicación 
@main_bp.route('/nuevo-registro', methods=['GET', 'POST'])
def nuevo_registro():
    if request.method == 'POST':
        if 'submitFormulario' in request.form:
            id_producto = request.form['idProducto']
            nombre = request.form['nombreProducto']
            proveedor = request.form['proveedorProducto']
            categoria = request.form['categoriaProducto']
            lote = request.form['loteProducto']
            cantidad = request.form['cantidadProducto']
            descripcion = request.form['descripcionProducto']

            new_register = Registro(id_producto=id_producto, nombre_producto=nombre, proveedor=proveedor, 
                                    categoria=categoria, lote=lote, cantidad=cantidad, descripcion=descripcion)
            db.session.add(new_register)
            db.session.commit()
    
    return render_template('main/nuevo_registro.html')    


@main_bp.route('/subir-csv', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        if 'submitCSV' in request.form:
            uploaded_file = request.files['csv_file']

            if uploaded_file.filename != '':
                csv_text = uploaded_file.read().decode('utf-8')
                csv_file = StringIO(csv_text)
                csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
                for row in csv_reader:
                    id_producto, producto, proveedor, categoria, lote, cantidad, descripcion = row

                    new_register = Registro(id_producto=id_producto, nombre_producto=producto, proveedor=proveedor, 
                                    categoria=categoria, lote=lote, cantidad=cantidad, descripcion=descripcion)
                    db.session.add(new_register)
                    db.session.commit()


                # Puedes realizar más procesamiento con los datos del CSV aquí

    return render_template('main/nuevo_registro.html')