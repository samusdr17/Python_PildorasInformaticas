def generaPares(limite):
	num=1

	while num<limite:
		
		yield num*2

		num=num+1

devuelve_Pares=generaPares(10)

print(next(devuelve_Pares))

print("Aquí podría ir más código...")

print(next(devuelve_Pares))

print("Aquí podría ir más código...")

print(next(devuelve_Pares))