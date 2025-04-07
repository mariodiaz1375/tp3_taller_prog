import random


def crear_vector_entero(cantidad):
    lista = []
    for i in range(cantidad):
        lista.append(random.randint(1,20))
    return lista 

def crear_vector_real(cantidad):
    lista = []
    for i in range(cantidad):
        numero = random.uniform(-10000, 10000)
        numero = round(numero, random.randint(0,5))
        lista.append(numero)
    return lista


if __name__ == '__main__':
    print(crear_vector_entero(5))
    print(crear_vector_real(7))
