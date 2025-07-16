# Código de Git: 

# Diccionarios con los datos del ejercicio.
# Estos guardan información que se va a utilizar en el código, como los modelos, sus características, precio, etc.
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1]
}

# Aquí verificamos que todos los modelos que están en productos también estén en stock, de lo contario muestra un mensaje en pantalla.
for modelo in productos:
    if modelo not in stock:
        print(f"Advertencia: el modelo {modelo} está en productos pero falta en stock.")


# Función para la opción 1, muestra el stock total de la marca.
def stock_marca(marca):
    total = 0  # Aquí se guarda la suma del stock.
    for modelo in productos:
        datos = productos[modelo]  # Obtenemos la lista de datos de ese modelo.
        marca_producto = datos[0]
        # Comparamos en minúsculas para evitar problemas con mayúsculas/minúsculas.
        if marca_producto.lower() == marca.lower():
            total += stock[modelo][1]  # Sumamos el stock.
    print(f"El stock total de la marca '{marca}' es: {total}")


# Función para la opción 2, busca modelos dentro de un rango de precios.
def busqueda_precio(p_min, p_max):
    resultados = []  # Lista para guardar los modelos que cumplen con lo de arriba.

    for modelo in productos:
        precio = stock[modelo][0]   # Obtenemos el precio.
        cantidad = stock[modelo][1]    # Obtenemos la cantidad en stock.

        # Revisamos si el precio está en el rango y si hay stock disponible.
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]  # Obtenemos la marca.
            resultados.append(f"{marca}--{modelo}")  # Agregamos en el formato pedido.

    resultados.sort()  # Esto es para ordenar alfabeticamente

    if len(resultados) == 0:
        print("No hay notebooks en ese rango de precios.")
    else:
        print("Modelos encontrados:")
        for item in resultados:
            print(item)


# Función para pedir el rango de precios y asegurarse que sean enteros.
def pedir_rango_precios():
    while True:  # Se repetirá hasta que el usuario ingrese bien el dato.
        try:
            p_min = int(input("Ingrese el precio mínimo (entero): "))
            p_max = int(input("Ingrese el precio máximo (entero): "))
            if p_min > p_max:
                print("El precio mínimo no puede ser mayor que el máximo. Intente de nuevo.")
                continue  # Vuelve a preguntar en caso de.
            return p_min, p_max  # Devuelve los valores correctos.
        except ValueError:
            print("Debe ingresar valores enteros.")


# Función para la opción 3, actualiza el precio de un modelo.
def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p  # Actualiza el precio.
        return True
    else:
        return False


# Función que gestiona la opción 3, pregunta datos y repite si el usuario quiere.
def opcion_actualizar_precio():
    while True:
        modelo = input("Ingrese el modelo que desea actualizar: ")
        try:
            precio_nuevo = int(input("Ingrese el nuevo precio (entero): "))
        except ValueError:
            print("Debe ingresar un número entero para el precio.")
            continue  # Vuelve a preguntar.

        exito = actualizar_precio(modelo, precio_nuevo)
        if exito:
            print("Precio actualizado.")
        else:
            print("El modelo no existe.")

        otra = input("¿Desea actualizar otro precio? (si/no): ").lower()
        if otra != "si":
            break  # Aquié se rompe el ciclo y vuele al menú.


# Función principal que muestra el menú y gestiona las opciones.
def menu_principal():
    while True:  # Se repite hasta que el usuario elige SALIR.
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")

        opcion = input("Ingresa una opción: ")

        if opcion == "1":
            marca_ingresada = input("Ingresa la marca que deseas consultar: ")
            stock_marca(marca_ingresada)

        elif opcion == "2":
            minimo, maximo = pedir_rango_precios()
            busqueda_precio(minimo, maximo)

        elif opcion == "3":
            opcion_actualizar_precio()

        elif opcion == "4":
            print("Programa finalizado.")
            break  # Termina el programa.

        else:
            print("Debe seleccionar una opción válida.")


# Llamamos a la función para que el programa comience.
menu_principal()
