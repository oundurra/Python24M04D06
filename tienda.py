from lista_producto import Lista_Producto, Lista_Producto_Restaurante
from abc import abstractmethod

class Tienda():
    def __init__(self, p_nombre, p_costo_delivery) -> None:
        self.__nombre = p_nombre
        self.__costo_delivery = p_costo_delivery
        self.__lista_productos = Lista_Producto()
    
    def agregar_producto(self, p_producto):
        self.__lista_productos.append(p_producto)

    def get_productos_tienda(self):
        return self.__lista_productos
    
    @abstractmethod
    def vender(self):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

class Farmacia(Tienda):
    def listar_productos(self):
        v_ret = ""
        for x in self.get_productos_tienda().get_lista_productos():
                v_ret = v_ret + f"{x.get_nombre()} {x.get_precio()} {'Envio gratis' if x.get_precio() > 15000 else ''} \n"
        return v_ret 
    
    def vender(self, p_nombre, p_cantidad):
        v_retorno_cod = -1
        v_retorno_msg = "Error no identificado"

        if p_cantidad > 3:
            v_retorno_cod = -1
            v_retorno_msg = "Cantidad supera el límite: 3"
        else:
            v_producto = self.get_productos_tienda().get_item_by_nombre(p_nombre)
            if p_cantidad > v_producto.get_stock():
                v_producto.set_stock(0)
            else:
                v_producto.set_stock(v_producto.get_stock() - p_cantidad)
        
            v_retorno_cod = 0
            v_retorno_msg = ""

        return v_retorno_cod,
           
class Supermercado(Tienda):
    def listar_productos(self):
        v_ret = ""
        for x in self.get_productos_tienda().get_lista_productos():
                v_ret = v_ret + f"{x.get_nombre()} {x.get_precio()} {'Pocos productos disponibles' if x.get_stock() < 10 else '' } \n"
        return v_ret 

    def vender(self, p_nombre, p_cantidad):
        v_retorno = ""

        v_producto = self.get_productos_tienda().get_item_by_nombre(p_nombre)
        if p_cantidad > v_producto.get_stock():
            v_producto.set_stock(0)
        else:
            v_producto.set_stock(v_producto.get_stock() - p_cantidad)

class Restaurante(Tienda):
    def __init__(self, p_nombre, p_costo_delivery) -> None:
        self.__nombre = p_nombre
        self.__costo_delivery = p_costo_delivery
        self.__lista_productos = Lista_Producto_Restaurante()    

    def listar_productos(self):
        v_ret = ""
        for x in self.get_productos_tienda().get_lista_productos():
                v_ret = v_ret + f"{x.get_nombre()} {x.get_precio()} {x.get_stock()} \n"
        return v_ret 