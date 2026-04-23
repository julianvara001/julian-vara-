import random

class Personaje:
    def __init__(self, nombre, vida, daño_max):
        self.nombre = nombre
        self.vida = vida
        self.daño_max = daño_max

    def atacar(self, objetivo):
        golpe = random.randint(1, self.daño_max)
        objetivo.vida -= golpe
        print(f"{self.nombre} ataca a {objetivo.nombre} por {golpe} de daño.")

    def mostrar_estado(self):
        print(f"{self.nombre} - Vida: {self.vida}")

heroe = Personaje(input("Nombre de tu héroe: "), 50, 15)
rival = Personaje("Sistema", 45, 12)

while heroe.vida > 0 and rival.vida > 0:
    heroe.mostrar_estado()
    rival.mostrar_estado()
    accion = input("¿Atacar? (s/n): ")
    if accion.lower() == "s":
        heroe.atacar(rival)
        if rival.vida > 0:
            rival.atacar(heroe)
    print("-" * 20)

if heroe.vida > 0:
    print("¡Victoria!")
else:
    print("Fuiste derrotado.")
print("GAME OVER")