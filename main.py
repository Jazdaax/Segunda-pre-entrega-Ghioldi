from paquete.cliente import Cliente
from paquete.producto import Producto

cliente1 = Cliente("Justo", "Ghioldi", "justoghioldi23@gmail.com", "12345678")
producto1 = Producto("Camiseta", 20)

cliente1.agregar_al_carrito(producto1)
