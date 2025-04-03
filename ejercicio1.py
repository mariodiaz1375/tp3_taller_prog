     
def ingresar_numero_entero():
    try:
        num = int(input("Ingrese un numero entero: "))
        return num
    except:
        print('Solo ingrese numeros enteros, se asignara el valor 0 (cero)')
        return 0
    
def ingresar_numero():
    try:
        num = float(input("Ingrese un numero: "))
        return num
    except:
        print('Solo ingrese numeros, se asignara el valor 0 (cero)')
        return 0
    
def crear_lista(cantidad):
    lista = []
    for i in range(1, cantidad+1):
        print(f'Numero {i}')
        numero = ingresar_numero()
        lista.append(numero)
    return lista

    
def mayor(lista):
    mayor = max(lista)
    return mayor


if __name__ == '__main__':
    lista = crear_lista(3)
    maximo = mayor(lista)
    print(f'El valor maximo de los numeros ingresados es {maximo}')
    
    
