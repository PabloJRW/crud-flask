from flask import render_template, request, flash
from sqlalchemy import func
from app.main import  main_bp
from app.models.models import Registro
from productos import productos
from app import db
import csv
from io import StringIO
import pandas as pd
from app.auth.auth_blueprint import login_required


# ENDPOINT A LA PÁGINA PARA VER LOS REGISTROS REALIZADOS
@main_bp.route('/historial')
@login_required
def historial():
    inventario = db.session.query(Registro).order_by(Registro.id.desc()).all()
    return render_template('main/historial.html', productos=inventario) 


# ENDPOINT A LA PÁGINA PARA INGRESAR MATERIALES
@main_bp.route('/nuevo-registro', methods=['GET', 'POST'])
@login_required
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
        
        flash('Registrado exitosamente!.', 'success')
    
    return render_template('main/nuevo_registro.html')    


##########################

# ENDPOINT DE LA PÁGINA INVENTARIO
@main_bp.route('/inventario')
@login_required
def inventario():
    # Realiza la consulta para sumar los valores por nombre
    inventario = db.session.query(Registro.nombre_producto, func.sum(Registro.cantidad)).group_by(Registro.nombre_producto).all()

    return render_template('/main/inventario.html', inventario=inventario)


@main_bp.route('/subir-csv', methods=['GET', 'POST'])
@login_required
def upload_csv():
    if request.method == 'POST':
        if 'submitCSV' in request.form:
            uploaded_file = request.files['csv_file']

            if uploaded_file.filename != '':
                try:
                    data = pd.read_csv(uploaded_file, header=0)
                    for _, row in data.iterrows():
                        #id_producto, producto, proveedor, categoria, lote, cantidad, descripcion = row

                        new_register = Registro(id_producto=row['id_producto'], 
                                                nombre_producto=row['producto'], 
                                                proveedor=row['proveedor'], 
                                                categoria=row['categoria'], 
                                                lote=row['lote'], 
                                                cantidad=row['cantidad'], 
                                                descripcion=row['descripcion'])
                        db.session.add(new_register)
                    db.session.commit()
                
                except Exception as e:
                    return f"Error al cargar archivo: {str(e)}"
                    


                # Puedes realizar más procesamiento con los datos del CSV aquí

    return render_template('main/nuevo_registro.html')