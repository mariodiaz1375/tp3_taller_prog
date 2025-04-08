import math
from crear_matriz import crear_matriz_cuadrada

def sumar_diagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma = suma + matriz[i][i]
    return suma

def eliminar_repetidos(lista):
    lista_nueva = []
    for elemento in lista:
        if elemento not in lista_nueva:
            lista_nueva.append(elemento)
    return lista_nueva


def lista_k(matriz):
    lista_k = []
    diagonal = sumar_diagonal(matriz)
    for lista in matriz:
        for num in lista:
            factorial = math.factorial(num)
            if factorial >= diagonal:
                lista_k.append(num)
    return lista_k

if __name__ == '__main__':
    a = crear_matriz_cuadrada(5)
    print('matriz')
    for fila in a:
        print(fila)
    print('suma de la diagonal')
    print(sumar_diagonal(a))
    print('lista de k elementos')
    lista = lista_k(a)
    print(lista)
    print('lista sin elementos repetidos')
    lista_sr = eliminar_repetidos(lista)
    print(lista_sr)
    print('lista ordenada de menor a mayor')
    lista_sr.sort()
    print(lista_sr)