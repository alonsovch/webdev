import pymysql

DB_NAME = 'tarea2'
DB_USER = 'cc5002'
DB_PASS = 'programacionweb'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_CHARSET = 'utf8'

def get_connection():
    conn = pymysql.connect(
        db=DB_NAME,
        user=DB_USER,
        passwd=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        charset=DB_CHARSET
    )
    return conn

def get_comuna_id(comuna):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM comuna WHERE nombre = %s", (comuna,))
    id = cursor.fetchone()
    cursor.close()
    conn.close()
    return id

def get_tipo_id(tipo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tipo_verdura_fruta WHERE nombre = %s", (tipo,))
    id = cursor.fetchone()
    cursor.close()
    conn.close()
    return id

def get_last_product_id():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM producto")
    last_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return last_id

def get_last_pedido_id():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM pedido")
    last_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return last_id
    
def registrar_producto(tipo, comuna_id, nombre_productor, email_productor, celular_productor, descripcion="",):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO producto (tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor) VALUES (%s, %s, %s, %s, %s, %s)", (tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor))
    conn.commit()
    cursor.close()
    conn.close() 

def registrar_pedido(tipo, comuna_id, nombre_comprador, email_comprador, celular_comprador, descripcion="",):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pedido (tipo, descripcion, comuna_id, nombre_comprador, email_comprador, celular_comprador) VALUES (%s, %s, %s, %s, %s, %s)", (tipo, descripcion, comuna_id, nombre_comprador, email_comprador, celular_comprador))
    conn.commit()
    cursor.close()
    conn.close()   

def registrar_producto_verdura_fruta(producto_id, tipo_verdura_fruta_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO producto_verdura_fruta (producto_id, tipo_verdura_fruta_id) VALUES (%s, %s)", (producto_id, tipo_verdura_fruta_id))
    conn.commit()
    cursor.close()
    conn.close()

def registrar_pedido_verdura_fruta(tipo_verdura_fruta_id, pedido_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pedido_verdura_fruta (tipo_verdura_fruta_id, pedido_id) VALUES (%s, %s)", (tipo_verdura_fruta_id, pedido_id))
    conn.commit()
    cursor.close()
    conn.close()

def registrar_foto(ruta_archivo, nombre_archivo, producto_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO foto (ruta_archivo, nombre_archivo, producto_id) VALUES (%s, %s, %s)", (ruta_archivo, nombre_archivo, producto_id))
    conn.commit()
    cursor.close()
    conn.close()

def get_productos_paginados(page, per_page):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    offset = (page - 1) * per_page
    cursor.execute("""
        SELECT p.id, p.tipo, GROUP_CONCAT(tpf.nombre) AS productos, r.nombre AS region, c.nombre AS comuna, f.nombre_archivo AS foto_nombre
        FROM producto p
        JOIN comuna c ON p.comuna_id = c.id
        JOIN region r ON c.region_id = r.id
        JOIN producto_verdura_fruta pvf ON p.id = pvf.producto_id
        JOIN tipo_verdura_fruta tpf ON pvf.tipo_verdura_fruta_id = tpf.id
        LEFT JOIN foto f ON p.id = f.producto_id
        GROUP BY p.id, p.tipo, r.nombre, c.nombre, f.nombre_archivo
        LIMIT %s OFFSET %s
    """, (per_page, offset))
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return productos

def get_pedidos_paginados(page, per_page):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    offset = (page - 1) * per_page
    cursor.execute("""
        SELECT p.id, p.tipo, p.nombre_comprador, GROUP_CONCAT(tpf.nombre) AS pedidos, r.nombre AS region, c.nombre AS comuna
        FROM pedido p
        JOIN comuna c ON p.comuna_id = c.id
        JOIN region r ON c.region_id = r.id
        JOIN pedido_verdura_fruta pvf ON p.id = pvf.pedido_id
        JOIN tipo_verdura_fruta tpf ON pvf.tipo_verdura_fruta_id = tpf.id
        GROUP BY p.id, p.tipo, p.nombre_comprador, r.nombre, c.nombre
        LIMIT %s OFFSET %s;
    """, (per_page, offset))
    pedidos = cursor.fetchall()
    cursor.close()
    conn.close()
    return pedidos

def get_total_productos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM producto")
    total_productos = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return total_productos

def get_producto_por_id(producto_id):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT p.tipo, p.nombre_productor, p.email_productor, p.celular_productor, GROUP_CONCAT(tpf.nombre) AS productos, r.nombre AS region, c.nombre AS comuna, f.nombre_archivo AS foto_nombre
        FROM producto p
        JOIN comuna c ON p.comuna_id = c.id
        JOIN region r ON c.region_id = r.id
        JOIN producto_verdura_fruta pvf ON p.id = pvf.producto_id
        JOIN tipo_verdura_fruta tpf ON pvf.tipo_verdura_fruta_id = tpf.id
        LEFT JOIN foto f ON p.id = f.producto_id
        WHERE p.id = %s
        GROUP BY p.id, p.tipo, r.nombre, c.nombre, f.nombre_archivo
    """, (producto_id,))
    producto = cursor.fetchone()
    cursor.close()
    conn.close()
    return producto


def get_pedido_por_id(pedido_id):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT p.tipo, p.nombre_comprador, p.email_comprador, p.celular_comprador, p.descripcion, GROUP_CONCAT(tpf.nombre) AS productos, r.nombre AS region, c.nombre AS comuna
        FROM pedido p
        JOIN comuna c ON p.comuna_id = c.id
        JOIN region r ON c.region_id = r.id
        JOIN pedido_verdura_fruta pvf ON p.id = pvf.pedido_id
        JOIN tipo_verdura_fruta tpf ON pvf.tipo_verdura_fruta_id = tpf.id
        WHERE p.id = %s
        GROUP BY p.id, p.tipo, p.descripcion, r.nombre, c.nombre
    """, (pedido_id,))
    pedido = cursor.fetchone()
    cursor.close()
    conn.close()
    return pedido

def get_total_productos_tipo_producto():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
    tpf.nombre AS tipo_verdura_fruta,
    COUNT(pvf.producto_id) AS total_productos
    FROM 
        producto_verdura_fruta pvf
    JOIN 
        tipo_verdura_fruta tpf ON pvf.tipo_verdura_fruta_id = tpf.id
    GROUP BY 
        tpf.nombre;
    """)
    total = cursor.fetchall()
    cursor.close()
    conn.close()
    result = [{'tipo_verdura_fruta': row[0], 'total_productos': row[1]} for row in total]
    return result

def get_total_pedidos_por_comuna():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
    c.nombre AS comuna,
    COUNT(p.id) AS total_pedidos
    FROM 
        pedido p
    JOIN 
        comuna c ON p.comuna_id = c.id
    GROUP BY 
        c.nombre;
    """)
    total = cursor.fetchall()
    cursor.close()
    conn.close()
    result = [{'comuna': row[0], 'total_pedidos': row[1]} for row in total]
    return result
