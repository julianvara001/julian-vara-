class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrar_estado(self):
        if self.nota >= 4:
            print("Estado: Aprobado")
        else:
            print("Estado: Libre")


alumno1 = Alumno()
alumno1.inicializar("Juan", 8)
alumno1.imprimir()
alumno1.mostrar_estado()