import random as ran

rodillos = [
    ['X', '0', '7', 'X', '0', '7', 'X', '0', '7'],
    ['0', '7', 'X', '0', '7', 'X', '0', '7', 'X'],
    ['7', 'X', '0', '7', 'X', '0', '7', 'X', '0']
]

def tirar_numero():
    numero = ran.randint(0,9)
    return numero

def mover_rodillo(rodillos, num1, num2, num3):
    resultado = []
    lista_r = []
    numeros = [num1, num2, num3]
    for i in range(len(rodillos)):
        rodillos[i] = rotar_fila[lista, numeros[i]]
        
    return rodillos

def rotar_fila(lista, num):
    for i in range(num):
        primero = lista[0]
        for j in range(len(lista)-1):
                lista[j] = lista[j+1]
        lista[8] = primero
    return lista

def jugar():
    while True:
        print('Presione 1 para tirar el primer numero')


# resultado = mover_rodillo(5,0,rodillos)
# for fila in resultado:
#     print(fila)

print('por fila')
lista = rotar_fila(rodillos[0], 5)
print(lista)

