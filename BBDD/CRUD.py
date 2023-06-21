from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
root.title("Practica CRUD")
# root.geometry("300x360")


miFrame=Frame(root)
miFrame.pack()
# miFrame.config(width="280", height="560")

# --------------Barra Menú--------------------

def conectar():
	global miConexion
	miConexion=sqlite3.connect("bbddCRUD")
	global miCursor
	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE CRUD (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(100),
			DIRECCION VARCHAR(100),
			COMENTARIO VARCHAR(100))
			''')
	except:
		pass

	# listUsuario=[
	# 	('dcqee','wdcc','dcd','awdc','sdcas'),
	# 	('dcqee','wdcc','dcd','awdc','sdcas'),
	# 	('dcqee','wdcc','dcd','awdc','sdcas'),
	# 	('dcqee','wdcc','dcd','awdc','sdcas'),
	# 	('dcqee','wdcc','dcd','awdc','sdcas')
		
	# ]
	# miCursor.executemany("INSERT INTO CRUD VALUES (NULL,?,?,?,?,?)", listUsuario)


	# miCursor.execute('''
	# 	CREATE TABLE CRUD (
	# 	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	# 	NOMBRE VARCHAR(50),
	# 	PASSWORD VARCHAR(50),
	# 	APELLIDO VARCHAR(100),
	# 	DIRECCION VARCHAR(100),
	# 	COMENTARIO VARCHAR(100))
	# ''')


def desconectar():
	miConexion.close()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbdd=Menu(barraMenu, tearoff=0)
bbdd.add_command(label="Conectar", command=lambda: conectar())
bbdd.add_command(label="Salir", command=lambda: desconectar())


def borrarCampos(borrar):
	allTextos=[textoNombre,textoPassword,textoApellido,textoDireccion,textoComentario]
	for item in allTextos:
		item.set(borrar)
	

borrar=Menu(barraMenu, tearoff=0)
borrar.add_command(label="Borrar campos", command=lambda: borrarCampos(''))


crud=Menu(barraMenu, tearoff=0)
crud.add_command(label="Crear", command='')
crud.add_command(label="Leer", command='')
crud.add_command(label="Actualizar", command='')
crud.add_command(label="Borrar", command='')


ayuda=Menu(barraMenu, tearoff=0)
ayuda.add_command(label="Licencia")
ayuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbdd)
barraMenu.add_cascade(label="Borrar", menu=borrar)
barraMenu.add_cascade(label="CRUD", menu=crud)
barraMenu.add_cascade(label="Ayuda", menu=ayuda)


# ------------- Campos Inputs -----------------

textoId=IntVar()
textoNombre=StringVar()
textoPassword=StringVar()
textoApellido=StringVar()
textoDireccion=StringVar()
textoComentario=StringVar()

campoId=Entry(miFrame, text="Id:", textvariable=textoId)
campoId.grid(row=0, column=1, padx=10, pady=10) #, columnspan=24
# campoId.config(background="white", justify="center")
# Label(root, text="Id:").pack()


campoNombre=Entry(miFrame, textvariable=textoNombre)
campoNombre.grid(row=1, column=1, padx=10, pady=10)
campoNombre.config(fg="red", justify="right")


campoPassword=Entry(miFrame, textvariable=textoPassword)
campoPassword.grid(row=2, column=1, padx=10, pady=10)
campoPassword.config(show="?")


campoApellido=Entry(miFrame, textvariable=textoApellido)
campoApellido.grid(row=3, column=1, padx=10, pady=10)
# campoApellido.config(background="white", justify="center")


campoDireccion=Entry(miFrame, textvariable=textoDireccion)
campoDireccion.grid(row=4, column=1, padx=10, pady=10)
# campoDireccion.config(background="white", justify="center")


campoComentario=Text(miFrame, width=16, height=5)
campoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=campoComentario.yview)
scrollVert.grid(row=5,column=2, sticky="nsew")

campoComentario.config(yscrollcommand=scrollVert.set)
# campoComentario.config(background="white", justify="center")

# ---------------- labels ---------------------------

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario:")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# --------------- Funciones CRUD ----------------------

def create():
	# tuplaUsuario=()
	usuario=(textoNombre.get(),textoPassword.get(),textoApellido.get(),textoDireccion.get(),textoComentario.get())
	listUsuario=[usuario]
	# for item in usuario:
	# 	item = item.get()
	# 	listUsuario[0].append(item)
	# listUsuario.append(tuplaUsuario)

	print(listUsuario)

	miCursor.executemany("INSERT INTO CRUD VALUES (NULL,?,?,?,?,?)", listUsuario)
	miConexion.commit()

def delete():
	# miCursor.execute("DELETE FROM CRUD WHERE ID=textoID")
	for item in miCursor.execute('SELECT * FROM CRUD ORDER BY ID'):
		print(item)
	
# miConexion=sqlite3.connect("bbddCRUD")
# miCursor = miConexion.cursor()
# for item in miCursor.execute('SELECT * FROM CRUD ORDER BY ID'):
# 	print(item)

def update(campoA_modificar, variableA_modificar, campoDeBusqueda, variableBusqueda):
	variableA_modificar=""
	variableBusqueda=""

# ---------Primer intento -----------
	if(textoNombre.get()!=""):
		variableA_modificar=textoNombre
		valor = messagebox.askokcancel("OK", "Cancelar")
		if valor==True:
			miCursor.execute("UPDATE CRUD SET campoA_modificar=variableA_modificar WHERE campoDeBusqueda=variableBusqueda")
	if(textoPassword.get()!=""):
		variableA_modificar=textoPassword
	if(textoApellido.get()!=""):
		variableA_modificar=textoApellido
	if(textoDireccion.get()!=""):
		variableA_modificar=textoDireccion
	if(textoComentario.get()!=""):
		variableA_modificar=textoComentario

# --------- Segundo intento -----------
	# if(textoNombre.get()!=""):
	# 	campoA_modificar=textoNombre

	# if(textoPassword.get()!=""):
	# 	campoA_modificar=textoPassword
	# if(textoApellido.get()!=""):
	# 	campoA_modificar=textoApellido
	# if(textoDireccion.get()!=""):
	# 	campoA_modificar=textoDireccion
	# if(textoComentario.get()!=""):
	# 	campoA_modificar=textoComentario


	miCursor.execute("UPDATE CRUD SET campoA_modificar=variableA_modificar WHERE campoDeBusqueda=variableBusqueda")

# --------------- Botones CRUD ----------------------
miFrame2=Frame(root)
miFrame2.pack()

botonCreate=Button(miFrame2, text="Create", command=lambda: create())
botonCreate.grid(row=1, column=0, pady=10, padx=10)

botonRead=Button(miFrame2, text="Read", command='')
botonRead.grid(row=1, column=1, pady=10, padx=10)

botonUpdate=Button(miFrame2, text="Update", command=lambda: delete())
botonUpdate.grid(row=1, column=2, pady=10, padx=10)

botonDelete=Button(miFrame2, text="Delete", command='')
botonDelete.grid(row=1, column=3, pady=10, padx=10)



root.mainloop()