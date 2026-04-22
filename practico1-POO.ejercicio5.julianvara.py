class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        opcion = 0
        while opcion != 5:
            print("\n1. Añadir contacto\n2. Lista de contactos\n3. Buscar contacto\n4. Editar contacto\n5. Cerrar agenda")
            opcion = int(input("Elija una opción: "))
            if opcion == 1: self.añadir()
            elif opcion == 2: self.listar()
            elif opcion == 3: self.buscar()
            elif opcion == 4: self.editar()

    def añadir(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        self.contactos.append({"nombre": nombre, "tel": telefono, "email": email})

    def listar(self):
        for c in self.contactos:
            print(f"{c['nombre']} - {c['tel']} - {c['email']}")

    def buscar(self):
        nom = input("Nombre a buscar: ")
        for c in self.contactos:
            if c['nombre'] == nom:
                print(f"Encontrado: {c['tel']} - {c['email']}")

    def editar(self):
        nom = input("Nombre a editar: ")
        for c in self.contactos:
            if c['nombre'] == nom:
                c['tel'] = input("Nuevo teléfono: ")
                c['email'] = input("Nuevo email: ")

mi_agenda = Agenda()
mi_agenda.menu()