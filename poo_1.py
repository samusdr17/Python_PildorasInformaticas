class Coche():

	def __init__(self):

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self, arrancamos):

		self.__enmarcha=arrancamos


		if(self.__enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return "El coche está en marcha"

		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo. no podemos arrancar"

		else:
			return "El coche está parado"



	def estado(self):
		print("El coche tiene ruedas ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, "y un largo de ",
			self.__largoChasis)

	def __chequeo_interno(self):
		print("realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			
			return True
		
		else:
		
			return False



miCoche=Coche() #Instanci de clase / "Cromañón" Ejemplarizar clase

# print("El largo del coche es: ", miCoche.largoChasis)
# print("El coche tiene ", miCoche.ruedas, "ruedas")
print(miCoche.arrancar(True))

miCoche.estado()

print("-------------A continuación creamos el segundo objeto---------------")

miCoche2=Coche()
# print("El largo del coche es: ", miCoche.largoChasis)
# print("El coche tiene ", miCoche.ruedas, "ruedas")
print(miCoche2.arrancar(False))

# miCoche2.ruedas=2     Al ser una propiedad encapsulada, la propiedad ruedas no puede modificarse

miCoche2.estado()

