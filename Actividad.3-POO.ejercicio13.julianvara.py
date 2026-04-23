import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def lanzar_dado(self):
        valor = random.randint(1, 6)
        self.puntos += valor
        print(f"{self.nombre} lanzó un {valor}. Total: {self.puntos}")

p1 = Jugador(input("Tu nombre: "))
p2 = Jugador("CPU")

for ronda in range(1, 4):
    print(f"\nRonda {ronda}")
    input("Presiona Enter para lanzar el dado...")
    p1.lanzar_dado()
    p2.lanzar_dado()

if p1.puntos > p2.puntos:
    print("\nGanaste por puntos.")
elif p1.puntos < p2.puntos:
    print("\nGanó la CPU.")
else:
    print("\nEmpate.")
print("GAME OVER")