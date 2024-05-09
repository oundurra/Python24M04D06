from producto import Producto

class ProductoRestaurante(Producto):
    def __init__(self, p_nombre, p_precio, p_stock) -> None:
        self.__nombre = p_nombre
        self.__precio = p_precio
        self.__stock = 0

