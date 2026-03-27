inventario = []

while True:
    print("=== MENÚ PRINCIPAL ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
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

    elif opcion == "2":
        print("Mostrar inventario")

    elif opcion == "3":
        print("Calcular estadísticas")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente nuevamente.\n")