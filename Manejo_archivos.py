from io import open

# archivo_texto=open("archivo.txt","w")

# frase="Estupendo día para estudiar Python \n el miércoles"

# archivo_texto.write(frase)

# archivo_texto.close()

##############################################

# archivo_texto=open("archivo.txt","r")

# texto=archivo_texto.read()

# archivo_texto.close()

# print(texto)

###############################################3


# archivo_texto=open("archivo.txt","r")

# lineas_texto=archivo_texto.readlines()

# archivo_texto.close()

# print(lineas_texto[1])

#############################################


# archivo_texto=open("archivo.txt","a")

# archivo_texto.write("\n siempre es una buena ocasión para estudiar Python")

# archivo_texto.close()

######################################3

# archivo_texto=open("archivo.txt","r") 

# # archivo_texto.seek(11)

# archivo_texto.seek(len(archivo_texto.readline()))

# print(archivo_texto.read())

#####################################

archivo_texto=open("archivo.txt","r+") # Lectura y escritura

archivo_texto.write("Comienzo del texto")

# print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines();

lista_texto[1]=" Esta línea ha sido includa desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()
####################################

