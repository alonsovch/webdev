from flask import Flask, render_template, request
from database.db import get_connection


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar-pedido')
def agregar_pedido():
    return render_template('agregar-pedido.html')

@app.route('/agregar-producto', method=('GET', 'POST'))
def agregar_producto():
    if request.method == 'GET':
        return render_template('agregar-producto.html')
    elif request.method == 'POST':
        tipo_producto = request.form['tipo-producto']
        producto = request.form['producto']
        descripcion = request.form['descripcion']
        multimedia = request.form['multimedia']
        region = request.form['region']
        comuna = request.form['comuna']
        nombre_productor = request.form['nombre-productor']
        email_productor = request.form['email-productor']
        numero_productor = request.form['numero-productor']
    else:
        return "Método no permitido"
    
    
@app.route('/informacion-pedido')
def informacion_pedido():
    return render_template('informacion-pedido.html')

@app.route('/informacion-producto')
def informacion_producto():
    return render_template('informacion-producto.html')

@app.route('/ver-pedidos')
def ver_pedidos():
    return render_template('ver-pedidos.html')

@app.route('/ver-productos')
def ver_productos():
    return render_template('ver-productos.html')

@app.route('/check_db')
def check_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM region")
        data = cursor.fetchall()
        cursor.close() 
        conn.close() 

        if data:
            print(data)
            return "Conexión exitosa a MySQL en Docker"
    except Exception as e:
        return f"Error de conexión: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)