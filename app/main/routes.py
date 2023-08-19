from flask import render_template, request
from . import  main_bp
from productos import productos


@main_bp.route('/')
@main_bp.route('/registro')
def registro():
    return "Registro endpoint"
    #return render_template('main/registro.html', productos=productos) 


# Rutas de la aplicación 
@main_bp.route('/registrar', methods=['GET', 'POST'])
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
    
    return render_template('main/index.html')