import filetype
import re
import database.db as db

def validate_img(img):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    ALLOWED_MIMETYPES = {'image/png', 'image/jpeg', 'image/gif'}
    if img is None:
        return False
    if img.filename == '':
        return False  
    ftype_guess = filetype.guess(img)
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    return True

def validate_tipo_producto(tipo_producto):
     return tipo_producto in ['Fruta', 'Verdura']

def validate_productos(productos):
    if len(productos) > 5 and len(productos) < 1:
        return False
    conn = db.get_connection()
    cursor = conn.cursor()
    for producto in productos:
        cursor.execute("SELECT * FROM tipo_verdura_fruta WHERE nombre = %s", (producto,))
        resultado = cursor.fetchall()
        if not resultado:
            return False
    return True
         
def validate_multimedia(multimedia):
    if len(multimedia) > 3 and len(multimedia) < 1:
        return False
    for img in multimedia:
        if not validate_img(img):
            return False
    return True

def validate_region(region):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM region WHERE nombre LIKE %s", ("%" + region + "%",))
    resultados = cursor.fetchall()
    return len(resultados) != 0
    
def validate_comuna(comuna, region):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM comuna WHERE nombre LIKE %s AND region_id = (SELECT id FROM region WHERE nombre LIKE %s)", ("%" + comuna + "%", "%" + region + "%"))
    resultados = cursor.fetchall()
    return len(resultados) != 0


def validate_nombre_productor(nombre_productor):
    return (nombre_productor != '') and (len(nombre_productor) < 81) and (len(nombre_productor) > 2)

def validate_email_productor(email_productor):
    email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return email_productor != '' and bool(re.match(email_regex, email_productor))

def validate_numero_productor(numero_productor):
    numero_regex = r"^569\d{8}$" 
    return numero_productor != '' and bool(re.match(numero_regex, numero_productor))

