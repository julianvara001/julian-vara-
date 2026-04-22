class Triangulo:
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"Lado mayor: {mayor}")

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Tipo: Equilátero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Tipo: Isósceles")
        else:
            print("Tipo: Escaleno")

triangulo1 = Triangulo()
triangulo1.inicializar(10, 10, 5)
triangulo1.imprimir_mayor()
triangulo1.tipo_triangulo()