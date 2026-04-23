class Inventario:
    def __init__(self):
        self.objetos = []

    def gestionar(self, objeto):
        print(f"\nEncontraste: {objeto}")
        opcion = input("1. Guardar | 2. Usar | 3. Descartar: ")
        if opcion == "1":
            self.objetos.append(objeto)
        elif opcion == "2":
            print(f"Has usado {objeto}.")
        else:
            print("Objeto descartado.")

    def mostrar(self):
        print(f"Tu inventario actual: {self.objetos}")

mochila = Inventario()
items = ["Espada", "Poción", "Escudo", "Llave"]

for item in items:
    mochila.gestionar(item)
    mochila.mostrar()

print("GAME OVER")