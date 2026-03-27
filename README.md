# Sistema de Gestión de Inventario

Sistema de consola desarrollado en Python para el registro de productos, visualización de inventario y cálculo de estadísticas básicas de stock.

---

## Características

- Registro de productos con nombre, precio y cantidad.
- Visualización del inventario completo.
- Cálculo del valor total del inventario y cantidad total de unidades.
- Menú interactivo en consola.

---

## Requisitos

- Python 3.x

No requiere librerías externas.

---

## Ejecución

```bash
python main.py
```

---

## Uso

Al ejecutar el programa se presenta el siguiente menú:

```
=== MENÚ PRINCIPAL ===
1. Agregar producto
2. Mostrar inventario
3. Calcular estadísticas
4. Salir
```

### Opción 1 - Agregar producto

Solicita el nombre, precio y cantidad del producto y lo almacena en el inventario.

```
Ingrese el nombre del producto: Manzanas
Ingrese el precio: 2.50
Ingrese la cantidad: 100
Producto agregado correctamente.
```

### Opción 2 - Mostrar inventario

Lista todos los productos registrados con su precio y cantidad.

```
--- INVENTARIO ---
Producto: Manzanas | Precio: 2.5 | Cantidad: 100
```

### Opción 3 - Calcular estadísticas

Muestra el valor total del inventario (precio x cantidad por producto) y la cantidad total de unidades registradas.

```
--- ESTADÍSTICAS ---
Valor total del inventario: 250.0
Cantidad total de productos: 100
```

### Opción 4 - Salir

Finaliza la ejecución del programa.

---

## Estructura del código

```
main.py
│
├── inventario              # Lista global que almacena los productos
├── agregar_producto()      # Registra un nuevo producto en el inventario
├── mostrar_inventario()    # Imprime todos los productos registrados
├── calcular_estadisticas() # Calcula valor total y cantidad total de unidades
└── while True (menú)       # Bucle principal de navegación
```

---

## Notas

- El inventario se almacena en memoria. Los datos no persisten al cerrar el programa.
- Los precios se ingresan como números decimales y las cantidades como enteros.
