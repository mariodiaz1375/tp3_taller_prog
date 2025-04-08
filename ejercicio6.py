from crear_matriz import crear_matriz, crear_matriz_cuadrada

from ejercicio1 import ingresar_numero, ingresar_numero_entero


def comprobar_producto(a, b):
    if len(a[0]) == len(b):
        return True
    else:
        return False

def crear_matriz_producto(a, b):
    matriz_p = []
    for i in range(len[a]):
        for j in range(len(b[0])):
            matriz_p[i][j] = 0

def columna_a_lista(matriz):
    columnas = []
    for i in range(len(matriz[0])):
        columna = []
        for lista in matriz:
            columna.append(lista[i])
        columnas.append(columna)
    return columnas
        
def crear_matriz_producto(a, b):
    matriz_p = crear_matriz(len(a), len(b[0]))
    for i in range(len(matriz_p)):
        for j in range(len(matriz_p[i])):
            matriz_p[i][j] = 0
    return matriz_p

def sumar_matrices(a, b):
    matriz = a
    for i in range(len(a)):
        for j in range(len(a[i])):
            matriz[i][j] = a[i][j] + b[i][j]
    return matriz

def multiplicar_matrices(a, b):
    matriz_p = crear_matriz_producto(a,b)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                matriz_p[i][j] += a[i][k] * b[k][j]
    return matriz_p

if __name__ == '__main__':

    matriz1 = crear_matriz(2,3)
    matriz2 = crear_matriz(3,2)
    print('\nMatriz 1: ')
    for fila in matriz1:
        print(fila)

    print('\nMatriz 2: ')
    for fila in matriz2:
        print(fila)
    
    # print('\nResultado de la suma de a + b')   
    # resultado = sumar_matrices(matriz1,matriz2)
    # for fila in resultado:
    #     print(fila)

    print('producto')
    print(crear_matriz_producto(matriz1, matriz2))
    print('resultado: ')
    matriz_p = multiplicar_matrices(matriz1, matriz2)
    for fila in matriz_p:
        print(fila)

    columnas = columna_a_lista(matriz2)
    for columna in columnas:
        print(columna)