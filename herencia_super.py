class Persona():

	def __init__(self, nombre, edad, Lugar_residencia):

		self.nombre=nombre

		self.edad=edad

		self.Lugar_residencia=Lugar_residencia

	def descripcion(self):

		print("Nombre: ", self.nombre, "Edad: ", self.edad, " Residencia: ", self.Lugar_residencia)

class Empleado(Persona):

	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, redidencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, redidencia_empleado)

		self.salario=salario

		self.antigüedad=antigüedad

	def descripcion(self):

		super().descripcion()

		print(" Salario: ", self.salario, " Antigüedad: ", self.antigüedad)



Manuel=Persona("Manuel", 55, "Colombia") #Un objeto Empleado siempre a de ser Persona, no siendo igual de forma contraria.

Manuel.descripcion()

print(isinstance(Manuel, Empleado))

