class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    def mostrar_informacion(self):
        print("Cuenta de Caja de Ahorro:")
        self.imprimir()

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def obtener_importe_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar_informacion(self):
        print("Cuenta de Plazo Fijo:")
        self.imprimir()
        print(f"Plazo: {self.plazo} días")
        print(f"Interés: {self.interes}%")
        print(f"Total interés: {self.obtener_importe_interes()}")

caja = CajaAhorro("Dario", 5000)
caja.mostrar_informacion()

plazo = PlazoFijo("Maria", 10000, 30, 0.75)
plazo.mostrar_informacion()