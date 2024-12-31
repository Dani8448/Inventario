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
def main():
    while True:
        print("\nMenú de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Eliminar producto")
        print("4. Consultar inventario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            modificar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == "4":
            mostrar_inventario()
        elif opcion == "5":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
