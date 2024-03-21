import sqlite3
def buscartodo():
    con = sqlite3.connect("Basededatosapp.db")
    cur = con.cursor()
    cur.execute("")

def tabla():
    con = sqlite3.connect("Basededatosapp.db")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE 'VENTAS'(
                'Cantidad' INTEGER,
                'id_compra' INTEGER,
                'Metodo'   Text,
                PRIMARY KEY('id_compra' AUTOINCREMENT)

    )""")
    con.close()
def buscartodo():
    con = sqlite3.connect("Basededatosapp.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM VENTAS")
    resultado = cursor.fetchall()
    return resultado