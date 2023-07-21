# def num_mayor_inf():
# 	inp = int(input("Introduce un número: "))
# 	cont=0
# 	while inp>=cont:
# 		cont = inp+1
# 		inp = int(input("Introduce un número: "))
	
# print(num_mayor_inf())




def sum_num_posit():
	list = []
	var=int(input("Introduce un número: "))
	while var>=0:
		list.append(var)
		var=int(input("Introduce un número: "))
	return(sum(list))
print(sum_num_posit())