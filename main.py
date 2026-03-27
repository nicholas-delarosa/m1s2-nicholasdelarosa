inventario = []

print("=== MENÚ PRINCIPAL ===")
print("1. Agregar producto")
print("2. Mostrar inventario")
print("3. Calcular estadísticas")
print("4. Salir")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    print("Agregar producto")
elif opcion == "2":
    print("Mostrar inventario")
elif opcion == "3":
    print("Calcular estadísticas")
elif opcion == "4":
    print("Saliendo del sistema...")
else:
    print("Opción inválida. Intente nuevamente.")