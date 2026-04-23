import random

class Cofre:
    def __init__(self):
        self.abierto = False
        self.monedas = random.randint(20, 50)

    def abrir(self):
        if not self.abierto:
            self.abierto = True
            return self.monedas
        return 0

class Explorador:
    def __init__(self):
        self.monedas_totales = 0

    def recolectar(self, cantidad):
        self.monedas_totales += cantidad
        print(f"Monedas acumuladas: {self.monedas_totales}")

jugador = Explorador()
continuar = "s"

while continuar == "s":
    print("\nEncuentras un cofre.")
    opcion = input("¿Abrir cofre (a) o seguir explorando (s)?: ")
    if opcion.lower() == "a":
        cofre_nuevo = Cofre()
        premio = cofre_nuevo.abrir()
        jugador.recolectar(premio)
    
    continuar = input("¿Seguir en la cueva? (s/n): ")

print(f"Resultado final: {jugador.monedas_totales} monedas.")
print("GAME OVER")