def crear_registro():
    registro = []
    try: 
        print('\nCargando un producto')
        producto = input('Ingrese el nombre del producto: ')
        marca = input('Ingrese el proveedor: ')
        precio = float(input("ingrese el precio del producto: "))
        stock = int(input('Ingrese la cantidad: '))
        registro = [producto, marca, str(precio), str(stock)]
        return registro
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        return registro
    
def mostrar_por_prov(matriz):
    prov = input('\nIngrese el proveedor: ')
    print(f'Productos del proveedor {prov}: ')
    for registro in matriz:
        if registro[1] == prov:
            print(registro[0])

def mostrar_mas_barato(matriz):
    print('\nProducto mas barato: ')
    precio = float(matriz[0][2])
    for registro in matriz:
        if float(registro[2]) < precio:
            precio = float(registro[2])
    for registro in matriz:
        if float(registro[2]) == precio:
            print(registro)
    
def mostrar_existente(matriz):
    print('\nProductos con existencias: ')
    for registro in matriz:
        if float(registro[3]) > 0:
            print(registro) 


def desplegar_menu():
    matriz = []
    try:
        while True:
            print('\n1. Agregar un producto')
            print('2. Mostrar productos por proveedor')
            print('3. Mostrar el producto mas barato')
            print('4. Mostrar los productos con existencias')
            print('5. Mostrar todos los productos')
            print('6. Salir')
            opcion = input('Ingrese una opcion: ')

            if opcion == '1':
            
                producto = crear_registro()
                if producto:
                    matriz.append(producto)
                    print('Producto agergado correctamente')
                else:
                    print('Producto no agregado, intentelo de nuevo')

            elif opcion == '2':

                mostrar_por_prov(matriz)

            elif opcion == '3':

                mostrar_mas_barato(matriz)

            elif opcion == '4':

                mostrar_existente(matriz)

            elif opcion == '5':
                
                print('\nTodos los productos')
                for producto in matriz:
                    print(producto)

            elif opcion == '6':
                break

            else:
                print('Ingrese una opcion valida')
    except Exception as e:
        print(f'Ocurrio un error: {e}')


if __name__ == '__main__':
    desplegar_menu()

