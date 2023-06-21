import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

# -----------Bloque generador de campos en tabla e inserto primeros artículos-----------

# -----------bloque 1 eligiendo un campo clave-----------------
# miCursor.execute('''
# 	CREATE TABLE PRODUCTOS (
# 	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
# 	NOMBRE_ARTICULO VARCHAR(50),
# 	PRECIO INTEGER,
# 	SECCION VARCHAR(20))
# 		''')

# productos=[

# 	("AR01", "pelota", 20, "jugueteria"),
# 	("AR02", "pantalón", 15, "confección"),
# 	("AR03", "destornillador", 25, "ferretería"),
# 	("AR04", "jarrón", 45, "cerámica")
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR06', 'estopín', 17, 'tienda de pirotecnia')")

# -----------bloque 2 campo clave autoincremental-----------------

# miCursor.execute('''
# 	CREATE TABLE PRODUCTOS (
# 	ID INTEGER PRIMARY KEY AUTOINCREMENT,
# 	NOMBRE_ARTICULO VARCHAR(50),
# 	PRECIO INTEGER,
# 	SECCION VARCHAR(20))
# 		''')

# productos=[

# 	("pelota", 20, "jugueteria"),
# 	("pantalón", 15, "confección"),
# 	("destornillador", 25, "ferretería"),
# 	("jarrón", 45, "cerámica")
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

# -----------bloque 3 claúsula unique-----------------

# miCursor.execute('''
# 	CREATE TABLE PRODUCTOS (
# 	ID INTEGER PRIMARY KEY AUTOINCREMENT,
# 	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
# 	PRECIO INTEGER,
# 	SECCION VARCHAR(20))
# 		''')

# productos=[

# 	("pelota", 20, "jugueteria"),
# 	("pantalón", 15, "confección"),
# 	("destornillador", 25, "ferretería"),
# 	("jarrón", 45, "cerámica"),
# 	("pantalones", 35, "confección")
# ]

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

# ----------Peticiones a la BBDD-----------------

# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")

# productos=miCursor.fetchall()

# print(productos)

# ----------Actualizaciones en la BBDD-----------------

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

# ----------Borrar en la BBDD-----------------

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")




miConexion.commit()

miConexion.close()