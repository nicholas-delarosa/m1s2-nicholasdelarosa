inventario = []

# Función para agregar productos al inventario
def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente.\n")


# Función para mostrar el inventario
def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.\n")
        return

    print("\n--- INVENTARIO ---")
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
    print()


# Función para calcular estadísticas
def calcular_estadisticas(inventario):
    if not inventario:
        print("No hay datos para calcular estadísticas.\n")
        return

    valor_total = 0
    cantidad_total = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        cantidad_total += producto["cantidad"]

    print("\n--- ESTADÍSTICAS ---")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {cantidad_total}\n")


# Menú principal con bucle infinito
while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto(inventario)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        calcular_estadisticas(inventario)

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente nuevamente.\n")


# Este programa permite registrar productos, almacenarlos en un inventario
# y calcular estadísticas básicas como el valor total y la cantidad total de productos.