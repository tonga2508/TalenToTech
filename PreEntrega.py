# Lista para almacenar los productos
inventario = []

# Variable para controlar el bucle del menú
opcion = ""

# Bucle que mantiene el menú activo hasta que el usuario elija salir
while opcion != "3":
    # Mostrar las opciones del menú
    print("=== Menú de Gestión de Productos ===")
    print("1. Agregar producto al inventario")
    print("2. Mostrar inventario")
    print("3. Salir")

    # Solicitar al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    # Opción 1: Agregar producto al inventario
    if opcion == "1":
        # Solicitar al usuario el nombre del producto
        nombre = input("Ingrese el nombre del producto: ")

        # Solicitar al usuario la cantidad del producto y validar que sea un entero positivo
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser mayor a 0. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

        # Crear un diccionario con el nombre y la cantidad del producto
        producto = {"nombre": nombre, "cantidad": cantidad}

        # Agregar el producto al inventario
        inventario.append(producto)

        # Confirmar que el producto ha sido agregado
        print(f"Producto '{nombre}' agregado con éxito.\n")

    # Opción 2: Mostrar inventario
    elif opcion == "2":
        # Verificar si el inventario está vacío
        if not inventario:
            print("El inventario está vacío.\n")
        else:
            print("\nInventario actual:")
            # Recorrer e imprimir cada producto en el inventario
            for producto in inventario:
                print(f"- {producto['nombre']}: {producto['cantidad']} unidades")
            print()  # Línea en blanco para separación

    # Opción 3: Salir del programa
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")

    # Opción inválida
    else:
        print("Opción inválida. Intente nuevamente.\n")
