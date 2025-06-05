# from curses.ascii import isalnum, isupper

# from curses.ascii import isalnum


inpName = input()
Prueba = "EstoE sUnaPrueba"

# def checkPassword(inpPassword):
#     if isalnum(inpPassword) is True:
#         print("La contraseña debe contener un carácter que no sea ni letra ni número")
#     elif len(inpPassword) <= 9:
#         print("la contraseña debe tener al menos 10 caracteres")
#     elif any(not isalnum(inpPassword)):
#         print("La contraseña debe contener al menos un carácter que no sea ni letra ni número")
#     elif all(isupper(inpPassword)) == True:
#         print("La contraseña no es segura")
#     for i in inpPassword:
#         if inpPassword[i] == " ":
#             print("La contraseña no puede contener espacios en blanco")
#             break
# print(checkPassword(Prueba))


# def checkPassword(inpPassword):
    
#     for i in inpPassword:
#         if i.isalnum() is True:
#             print("La contraseña debe contener un carácter que no sea ni letra ni número")
#         elif len(inpPassword) <= 9:
#             print("la contraseña debe tener al menos 10 caracteres")
#         elif any(not i.isalnum()):
#             print("La contraseña debe contener al menos un carácter que no sea ni letra ni número")
#         elif all(i.isupper()) == True:
#             print("La contraseña no es segura")
#         if inpPassword[i] == " ":
#             print("La contraseña no puede contener espacios en blanco")
#             break
# print(checkPassword(Prueba))

def checkPassword(inpPassword):
    if isalnum(inpPassword) is True:
        return "La contraseña debe contener un carácter que no sea ni letra ni número"
    elif len(inpPassword) <= 9:
        return "la contraseña debe tener al menos 10 caracteres"
    elif any(not isalnum(inpPassword)):
        return "La contraseña debe contener al menos un carácter que no sea ni letra ni número"
    elif all(isupper(inpPassword)) == True:
        return "La contraseña no es segura"
    elif " " in inpPassword:
        return "La contraseña no puede contener espacios en blanco"
    
    # for i in inpPassword:
    
    #     if inpPassword[i] == " ":
    #         print("La contraseña no puede contener espacios en blanco")
    
    #         break
print(checkPassword(Prueba))
        

            


