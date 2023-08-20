from flask import render_template, request
from app.main import  main_bp
#from app.models import models
from productos import productos


@main_bp.route('/registros')
def registros():
    #return "Registro endpoint"
    return render_template('main/registro.html', productos=productos) 


# Rutas de la aplicación 
@main_bp.route('/nuevo-registro', methods=['GET', 'POST'])
def nuevo_registro():
    if request.method == 'POST':
        id_ = request.form['idProducto']
        nombre = request.form['nombreProducto']
        proveedor = request.form['proveedorProducto']
        categoria = request.form['categoriaProducto']
        lote = request.form['loteProducto']
        cantidad = request.form['cantidadProducto']
        descripcion = request.form['descripcionProducto']

        producto= [id_, nombre, proveedor, categoria, lote, cantidad, descripcion]
    
    
    return render_template('main/nuevo_registro.html')    