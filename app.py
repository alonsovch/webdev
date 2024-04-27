# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar-pedido')
def agregar_pedido():
    return render_template('agregar-pedido.html')

@app.route('/agregar-producto')
def agregar_producto():
    return render_template('agregar-producto.html')

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

if __name__ == '__main__':
    app.run(debug=True)