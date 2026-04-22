class Persona:
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")

# Bloque principal
persona1 = Persona()
persona1.inicializar("Carlos", 25)
persona1.mostrar()
persona1.es_mayor_de_edad()

persona2 = Persona()
persona2.inicializar("Lucía", 15)
persona2.mostrar()
persona2.es_mayor_de_edad()