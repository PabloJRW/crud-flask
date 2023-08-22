from app import db


# Modelo para signup
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def __repr__(self):
        return f"<User: {self.username}>"
    

# Modelo para nuevos registros
class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    id_producto = db.Column(db.String, nullable=False)
    nombre_producto = db.Column(db.String, nullable=False)
    proveedor = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    lote = db.Column(db.String, nullable=False)   
    cantidad = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    #registrado_por = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, id_producto, nombre_producto, proveedor, categoria, lote, cantidad, descripcion):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.proveedor = proveedor
        self.categoria = categoria
        self.lote = lote
        self.cantidad = cantidad
        self.descripcion = descripcion
        #self.registrado_por = registrado_por

    def __repr__(self):
        return f"<Producto: {self.nombre_producto}>"