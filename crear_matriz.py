from crear_vector import crear_vector_entero

def crear_matriz_cuadrada(filas):
    matriz = []
    for i in range(filas):
        matriz.append(crear_vector_entero(filas))
    return matriz

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append(crear_vector_entero(columnas))
    return matriz

    