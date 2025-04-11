import random as ran

rodillos = [
    ['X', '0', '7', 'X', '0', '7', 'X', '0', '7'],
    ['0', '7', 'X', '0', '7', 'X', '0', '7', 'X'],
    ['7', 'X', '0', '7', 'X', '0', '7', 'X', '0']
]

def tirar_numero():
    numero = ran.randint(0,9)
    return numero

def mover_rodillo(num, rodillo, rodillos):
    for i in range(num):
        primero = rodillos[rodillo][0]
        for j in range(len(rodillos[rodillo])-1):
            rodillos[rodillo][j] = rodillos[rodillo][j+1]
        rodillos[rodillo][8] = primero
    return rodillos

def jugar():
    while True:
        print('Presione 1 para tirar el primer numero')


resultado = mover_rodillo(5,0,rodillos)
for fila in resultado:
    print(fila)

