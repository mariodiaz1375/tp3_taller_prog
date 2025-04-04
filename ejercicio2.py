from ejercicio1 import crear_lista, mayor


if __name__ == '__main__':
    lista = crear_lista(10)
    maximo = mayor(lista)
    print(f'El valor maximo de los numeros ingresados es {maximo}')