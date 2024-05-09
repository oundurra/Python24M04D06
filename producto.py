class Producto():
    def __init__(self, p_nombre: str, p_precio: int = 0, p_stock: int = 0) -> None:
        self.__nombre = p_nombre
        self.__precio = p_precio
        self.__stock = p_stock

    def __eq__(self, value) -> bool:
        return self.get_nombre() == value.get_nombre()

    def set_stock(self, p_stock: int):
        if p_stock < 0:
            self.__stock = 0
        else:
            self.__stock = p_stock

    def add_stock(self, p_units: int):
        v_new_stock = self.__stock - p_units

        if v_new_stock < 0:
            self.__stock = 0
        else:
            self.__stock = v_new_stock

    def get_stock(self) -> int:
        return self.__stock
    
    def get_nombre(self) -> str:
        return self.__nombre

    def get_precio(self) -> int:
        return self.__precio