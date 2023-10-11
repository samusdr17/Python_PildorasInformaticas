# for i in "juan@pildorasinformaticas.es":
# 	print("Hola", end=" ")



# email=False
# mi_Email=input("Introduce tu dirección de email: ")

# for i in mi_Email:
# 	if(i=="@"):
# 		email=True

# if email: #dejar la variable booleana sola, es lo mismo que email==True
# 	print("Email es correcto")
# else:
# 	print("El email no es correcto")
# 	############################################
# contador=0
# mi_Email=input("Introduce tu dirección de email: ")

# for i in mi_Email:
# 	if(i=="@" or i=="."):
# 		contador=contador+1

# if contador==2:
# 	print("Email es correcto")
# else:
# 	print("El email no es correcto")




# for i in range(5,50,3): #El tercer argumento marca cada cuantos muestra dentro del intervalo marcado.
# 	print(f"valor de la variable {i}")




valido=False

email=input("Introduce tu email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido:
	print("Email correcto")
else:
	print("Email incorrecto")