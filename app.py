from flask import Flask, render_template, request, url_for
import utils.validations as val
import database.db as db
from werkzeug.utils import secure_filename
import os
import flask

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
PRODUCTS_PER_PAGE = 5

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #16MB

@app.errorhandler(413)
def request_entity_too_large(error):
    return "Archivo demasiado grande", 413

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar-pedido', methods=['GET', 'POST'])
def agregar_pedido():
    if request.method == 'GET':
        return render_template('agregar-pedido.html')
    elif request.method == 'POST':
        tipo_producto = request.form['tipo-producto']
        producto = request.form.getlist('producto')
        descripcion = request.form['descripcion']
        region = request.form['region']
        comuna = request.form['comuna']
        nombre_comprador = request.form['nombre-comprador']
        email_comprador = request.form['email-comprador']
        numero_comprador = request.form['numero-comprador']
        if (val.validate_tipo_producto(tipo_producto) and val.validate_productos(producto) and val.validate_region(region) and val.validate_comuna(comuna, region) and val.validate_nombre_productor(nombre_comprador) and val.validate_email_productor(email_comprador) and val.validate_numero_productor(numero_comprador)):
            comuna_id = db.get_comuna_id(comuna)
            db.registrar_pedido(tipo_producto, comuna_id, nombre_comprador, email_comprador, numero_comprador, descripcion)
            pedido_id = db.get_last_pedido_id()
            for p in producto:
                tipo_id = db.get_tipo_id(p)
                db.registrar_pedido_verdura_fruta(tipo_id, pedido_id)
            return render_template('volver-inicio.html')
        else:
            return render_template('producto-no-agregado.html')
    else:
        return "Método no permitido"


@app.route('/agregar-producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'GET':
        return render_template('agregar-producto.html')
    elif request.method == 'POST':
        tipo_producto = request.form['tipo-producto']
        producto = request.form.getlist('producto')
        descripcion = request.form['descripcion']
        multimedia = flask.request.files.getlist('multimedia')
        region = request.form['region']
        comuna = request.form['comuna']
        nombre_productor = request.form['nombre-productor']
        email_productor = request.form['email-productor']
        numero_productor = request.form['numero-productor']
        if (val.validate_tipo_producto(tipo_producto) and val.validate_productos(producto) and val.validate_multimedia(multimedia) and val.validate_region(region) and val.validate_comuna(comuna, region) and val.validate_nombre_productor(nombre_productor) and val.validate_email_productor(email_productor) and val.validate_numero_productor(numero_productor)):
            comuna_id = db.get_comuna_id(comuna)
            db.registrar_producto(tipo_producto, comuna_id, nombre_productor, email_productor, numero_productor, descripcion)
            producto_id = db.get_last_product_id()
            for p in producto:
                tipo_id = db.get_tipo_id(p)
                db.registrar_producto_verdura_fruta(producto_id, tipo_id)
            for img in multimedia:
                filename = secure_filename(img.filename)
                route = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                img.save(route)
                db.registrar_foto(route, filename, producto_id)
            return render_template('volver-inicio.html')
        else:
            return render_template('producto-no-agregado.html')
    else:
        return "Método no permitido"
    
    
@app.route('/informacion-pedido')
def informacion_pedido():
    return render_template('informacion-pedido.html')

@app.route('/informacion-producto/<int:producto_id>')
def informacion_producto(producto_id):
    # Obtener la información del producto según su ID
    producto = db.get_producto_por_id(producto_id)
    return render_template('informacion-producto.html', producto=producto)

@app.route('/ver-pedidos')
def ver_pedidos():
    return render_template('ver-pedidos.html')

@app.route('/ver-productos')
def ver_productos():
    page = request.args.get('page', default=1, type=int)
    productos = db.get_productos_paginados(page, PRODUCTS_PER_PAGE)
    return render_template('ver-productos.html', productos=productos, page=page, per_page=PRODUCTS_PER_PAGE)

@app.route('/check_db')
def check_db():
    try:
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM region")
        data = cursor.fetchall()
        cursor.close() 
        conn.close() 

        if data:
            return "Conexión exitosa a MySQL en Docker"
    except Exception as e:
        return f"Error de conexión: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)