from ejercicio1 import ingresar_numero_entero

def sumar_numeros(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

def sumar_2_listas(A, B):
    resultado = []
    if len(A) == len(B):
        for i in range(len(A)):
            elemento = A[i] + B[i]
            resultado.append(elemento)
        return resultado
    else:
        print('Solo se pueden sumar listas con igual cantidad de elementos')
        return resultado
    
def crear_lista_enteros(cantidad):
    lista = []
    for i in range(1, cantidad+1):
        print(f'Numero {i}')
        numero = ingresar_numero_entero()
        lista.append(numero)
    return lista

if __name__ == '__main__':
    print('Crear lista a')
    a = crear_lista_enteros(3)
    print('\nCrear lista b')
    b = crear_lista_enteros(3)
    print(f'\nlista a: {a}')
    print(f'\nlista b: {b}')
    print('Resultado de sumar la lista a')
    print(sumar_numeros(a))
    print('Resultado de sumar la lista b')
    print(sumar_numeros(b))
    print('Resultado de sumar a+b')
    print(sumar_2_listas(a,b))

