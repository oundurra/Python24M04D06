from producto import Producto
from tienda import Tienda, Farmacia, Supermercado, Restaurante
from lista_producto import Lista_Producto

def listar_productos(p_tienda: Tienda):
    print("Productos")
    print("=========")
    print(p_tienda.listar_productos())
    
# Creación de la tienda
print("Creación de la tienda")
print("=====================")

nombre_tienda = input("Ingrese el nombre de la tienda: ")
costo_tienda = input("Ingrese el costo de envío de la tienda: ")

tipo_tienda = ""
while tipo_tienda not in ["F", "S", "R"]:
    tipo_tienda = input("Ingrese el tipo de tienda: [F]armacia, [S]upermercado, [R]estaurant: ")

# Ingreso de Productos
print("")
print("Ingreso de Productos")
print("====================")
respuesta = "S"
if tipo_tienda == "F":
    v_tienda = Farmacia(nombre_tienda, costo_tienda)
    while respuesta == "S":
        # Ingreso datos de producto
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))

        #Creo un producto con los datos ingresados
        v_prod = Producto(nombre, precio, stock)

        #Agrego el producto a la lista
        v_tienda.agregar_producto(v_prod)

        print("")

        respuesta = ""
        while respuesta not in ["S", "N"]:
            respuesta = input("Desea seguir ingresando productos [S],[N]: ")

        listar_productos(v_tienda)
elif tipo_tienda == "S":
    v_tienda = Supermercado(nombre_tienda, costo_tienda)
    while respuesta == "S":
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        v_prod = Producto(nombre, precio, stock)
        v_tienda.agregar_producto(v_prod)
        print("")
        
        respuesta = ""
        while respuesta not in ["S", "N"]:
            respuesta = input("Desea seguir ingresando productos [S],[N]: ")

        listar_productos(v_tienda)
elif tipo_tienda == "R":
    v_tienda = Restaurante(nombre_tienda, costo_tienda)
    while respuesta == "S":
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        v_prod = Producto(nombre, precio, stock)
        v_tienda.agregar_producto(v_prod)
        print("")
        
        respuesta = ""
        while respuesta not in ["S", "N"]:
            respuesta = input("Desea seguir ingresando productos [S],[N]: ")

        listar_productos(v_tienda)

# Ventas
print("")
print("Ingreso de Ventas")
print("=====================")
respuesta = ""
while respuesta not in ["S", "N"]:
    respuesta = input("Desea hacer una venta[S],[N]: ")

    if respuesta == "S":
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))

        v_venta_cod, v_venta_msg = v_tienda.vender(nombre, cantidad)

        if v_venta_cod < 0:
            print(v_venta_msg)
        
        respuesta = ""

listar_productos(v_tienda)
