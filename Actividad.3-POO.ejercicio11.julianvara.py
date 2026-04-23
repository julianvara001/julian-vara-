import random

class Hechicero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 40
        self.mana = 20

    def lanzar_hechizo(self, objetivo):
        if self.mana >= 5:
            daño = random.randint(10, 20)
            self.mana -= 5
            objetivo.vida -= daño
            print(f"{self.nombre} lanza magia a {objetivo.nombre} por {daño} de daño.")
        else:
            print(f"{self.nombre} no tiene suficiente mana.")

mago1 = Hechicero(input("Nombre del hechicero: "))
mago2 = Hechicero("Mago Oscuro")

while mago1.vida > 0 and mago2.vida > 0:
    print(f"\n{mago1.nombre} HP: {mago1.vida} Mana: {mago1.mana}")
    print(f"{mago2.nombre} HP: {mago2.vida}")
    
    opcion = input("¿Lanzar hechizo? (s/n): ")
    if opcion.lower() == "s":
        mago1.lanzar_hechizo(mago2)
        if mago2.vida > 0:
            mago2.lanzar_hechizo(mago1)

if mago1.vida > 0:
    print("¡Duelo ganado!")
else:
    print("Has perdido el duelo.")
print("GAME OVER")