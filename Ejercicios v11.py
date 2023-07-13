# def devuelvemeMax():
# 	num1=int(input("Introduce el primer numero: "))
# 	num2=int(input("Introduce el segundo numero: "))
# 	if num1>num2:
# 		return num1
# 	else:
# 		return num2

# print(devuelvemeMax())



# def contactUser():
# 	contactList=[]
# 	nombre=input("Introduce tu nombre: ")
# 	contactList.append(nombre)
# 	direccion=input("Introduce tu dirección: ")
# 	contactList.append(direccion)
# 	tlf=input("Introduce tu teléfono: ")
# 	contactList.append(tlf)
# 	if contactList[0] != "":
# 		return "Los datos almacenados son: " + contactList[0] + " " + contactList[1] + " " + contactList[2]
# 	else:
# 		return "¡¡Todos los datos son necesarios!!"

# print(contactUser())



def mediAritm():
	num1=int(input("Introduce el primer numero: "))
	num2=int(input("Introduce el segundo numero: "))
	num3=int(input("Introduce el tercer numero: "))
	return (num1+num2+num3)/3

print(mediAritm())