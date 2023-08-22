from flask import render_template, request
from app.main import  main_bp
from app.models.models import Registro
from productos import productos
from app import db


@main_bp.route('/registros')
def registros():
    #return "Registro endpoint"
    return render_template('main/registro.html', productos=productos) 


# Rutas de la aplicación 
@main_bp.route('/nuevo-registro', methods=['GET', 'POST'])
def nuevo_registro():
    if request.method == 'POST':
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