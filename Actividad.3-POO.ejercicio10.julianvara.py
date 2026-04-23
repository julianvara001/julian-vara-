import random

class Auto:
    def __init__(self, piloto):
        self.piloto = piloto
        self.distancia = 0

    def avanzar(self):
        pasos = random.randint(5, 15)
        self.distancia += pasos
        print(f"{self.piloto} avanzó hasta los {self.distancia}m.")

usuario = Auto(input("Nombre del piloto: "))
rival = Auto("Rival CPU")

while usuario.distancia < 100 and rival.distancia < 100:
    input("Presiona Enter para acelerar...")
    usuario.avanzar()
    rival.avanzar()
    print("-" * 10)

if usuario.distancia >= 100:
    print("¡Ganaste la carrera!")
else:
    print("El rival ganó.")
print("GAME OVER")