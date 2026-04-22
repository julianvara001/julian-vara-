class Calculadora:
    def __init__(self):
        self.valor1 = int(input("Ingrese primer valor: "))
        self.valor2 = int(input("Ingrese segundo valor: "))

    def sumar(self):
        print(f"Suma: {self.valor1 + self.valor2}")

    def restar(self):
        print(f"Resta: {self.valor1 - self.valor2}")

    def multiplicar(self):
        print(f"Multiplicación: {self.valor1 * self.valor2}")

    def dividir(self):
        if self.valor2 != 0:
            print(f"División: {self.valor1 / self.valor2}")
        else:
            print("No se puede dividir por cero.")

calc = Calculadora()
calc.sumar()
calc.restar()
calc.multiplicar()
calc.dividir()