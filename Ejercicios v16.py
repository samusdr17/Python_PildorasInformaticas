# def impares():
# 	list = []
# 	for i in range(1,100,2):
# 		list.append(i)
# 	return list

# print(impares())



def password():
	cont=0
	contraseña = input("Introduce tu contraseña: ")
	for i in range(len(contraseña)):
		if (contraseña[i] == " "):
			cont+=1
	if(len(contraseña) < 8 and cont > 1):
		return("Contraseña erronea")
	else:
		return("Contraseña OK")

print(password())




# def email():
# 	cont1=0
# 	cont2=0
# 	email = input("Introduce tu email: ")
# 	for i in range(len(email)):
# 		if (email[i] == "@"):
# 			cont1+=1
# 		elif(email[i] == "."):
# 			cont2+=1
# 	print(cont1)
# 	print(cont2)
# 	if (cont1==1 and cont2>=1):
# 		return("Email correcto")
# 	else:
# 		return("Email no válido")

# print(email())

