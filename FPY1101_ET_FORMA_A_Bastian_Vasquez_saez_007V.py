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
    '8475HD': [387900, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749090, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}

def stock_marca(marca):
    total = 0
    marca_lower = marca.lower()
    for modelo, info in productos.items():
        if info[0].lower() == marca_lower:
            if modelo in stock:
                total += stock[modelo][1]
    print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, datos in stock.items():
        precio = datos[0]
        cantidad = datos[1]
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}–{modelo}")
    resultados.sort()
    if resultados:
        print("Los notebooks entre los precios consultados son:", resultados)
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    return False

def mostrar_menu():
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

while True:
    mostrar_menu()
    opcion = input("Ingrese opción: ")
    
    try:
        opcion = int(opcion)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        continue
    
    if opcion == 1:
        marca = input("Ingrese marca a consultar: ")
        stock_marca(marca)
    
    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                busqueda_precio(p_min, p_max)
                break
            except ValueError:
                print("Debe ingresar valores enteros!!")
    
    elif opcion == 3:
        while True:
            modelo = input("Ingrese modelo a actualizar: ")
            try:
                precio = int(input("Ingrese precio nuevo: "))
            except ValueError:
                print("Debe ingresar valores enteros!!")
                continue
                
            if actualizar_precio(modelo, precio):
                print("Precio actualizado!!")
            else:
                print("El modelo no existe!!")
            
            respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
            if respuesta not in ('s', 'si'):
                break
    
    elif opcion == 4:
        print("Programa finalizado.")
        break
    
    else:
        print("Debe seleccionar una opción válida!!!")
