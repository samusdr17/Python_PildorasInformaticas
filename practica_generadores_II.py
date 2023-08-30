def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		# for subElemento in elemento: #Este for aninado con la instrucción yield subElemento muestra el mismo resultado que el codigo actual
			# yield elemento # Este yield es para el resultado normal esperado con el for actual.
			yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))