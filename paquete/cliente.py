class Cliente:
    def __init__(self, nombre, apellido, email, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.dni = dni
        self.carrito = []

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)

    def quitar_del_carrito(self, producto):
        if producto in self.carrito:
            self.carrito.remove(producto)

    def vaciar_carrito(self):
        self.carrito = []

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni} - {self.email}"
