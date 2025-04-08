from crear_vector import crear_vector_entero, crear_vector_natural

def crear_matriz_cuadrada(filas):
    matriz = []
    for i in range(filas):
        matriz.append(crear_vector_natural(filas))
    return matriz

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append(crear_vector_entero(columnas))
    return matriz

def crear_matriz_natural(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append(crear_vector_natural(columnas))
    return matriz

    