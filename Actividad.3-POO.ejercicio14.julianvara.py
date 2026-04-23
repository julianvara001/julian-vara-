import random

class Torre:
    def __init__(self):
        self.resistencia = 30

    def recibir_ataque(self):
        daño = random.randint(5, 10)
        self.resistencia -= daño
        print(f"¡Impacto! La torre pierde {daño} de resistencia.")

    def mostrar_estado(self):
        print(f"Resistencia de la torre: {self.resistencia}")

torre_defensa = Torre()

while torre_defensa.resistencia > 0:
    torre_defensa.mostrar_estado()
    accion = input("¿Reparar un poco (r) o esperar ataque (e)?: ")
    if accion.lower() == "r":
        torre_defensa.resistencia += 3
        print("Reparación mínima realizada.")
    
    print("Viene una oleada enemiga...")
    torre_defensa.recibir_ataque()
    print("-" * 20)

print("La torre ha caído.")
print("GAME OVER")