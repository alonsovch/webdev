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
    
