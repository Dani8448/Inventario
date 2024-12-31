from producto import Producto

productos = []

def agregar_producto(nombre, cantidad, precio):
    global productos
    if any(p.nombre == nombre for p in productos):
        print("Error: El producto ya existe.")
        return
    productos.append(Producto(nombre, cantidad, precio))
    print("Producto agregado correctamente.")

def modificar_producto(nombre, cantidad, precio):
    for producto in productos:
        if producto.nombre == nombre:
            producto.cantidad = cantidad
            producto.precio = precio
            print("Producto modificado correctamente.")
            return
    print("Error: Producto no encontrado.")

def eliminar_producto(nombre):
    global productos
    productos = [p for p in productos if p.nombre != nombre]
    print("Producto eliminado correctamente.")

def mostrar_inventario():
    if not productos:
        print("El inventario está vacío.")
    else:
        for producto in productos:
            print(producto)
