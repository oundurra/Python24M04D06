from producto import Producto

class Lista_Producto():
    def __init__(self):
        self.__productos = []

    def __sizeof__(self) -> int:
        return len(self.__productos)

    def append(self, p_producto: Producto):
        index = self.get_index(p_producto)

        if index is False:
            self.__productos.append(p_producto)
        else:
            self.__productos[index].set_stock(p_producto.get_stock())

    def get_index(self, p_producto: Producto):
        v_retorno = False
        if p_producto in self.__productos:
            v_retorno = self.__productos.index(p_producto)
        
        return v_retorno
    
    def get_item(self, p_producto: Producto):
        index = self.get_index(p_producto)

        if index >= 0:
            v_retorno = self.__productos[index]
        else:
            v_retorno = ""
        
        return v_retorno

    def get_item_by_nombre(self, p_nombre: str):
        return self.get_item(Producto(p_nombre))

    def get_lista_productos(self):
        return self.__productos


class Lista_Producto_Restaurante(Lista_Producto):
    def append(self, p_producto: Producto):
        index = self.get_index(p_producto)
        p_producto.set_stock = 0

        if index is False:
            self.__productos.append(p_producto)
        else:
            self.__productos[index].set_stock(0)