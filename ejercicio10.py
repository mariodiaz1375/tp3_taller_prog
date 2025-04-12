import random as ran


def crear_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        numeros.append(ran.randint(0,9))
    return numeros

def mover_rodillo(rodillos, numeros):
    resultado = []
    for i in range(len(rodillos)):
        resultado.append(rotar_fila(rodillos[i], numeros[i]))
    return resultado

def rotar_fila(lista, num):
    for i in range(num):
        primero = lista[0]
        for j in range(len(lista)-1):
                lista[j] = lista[j+1]
        lista[8] = primero
    return lista

def ganar(rodillos):
    if rodillos[0][0] == rodillos[1][0] == rodillos[2][0]:
        return True
    else:
        return False

def jugar():
    rodillos = [
        ['X', '0', '7', 'X', '0', '7', 'X', '0', '7'],
        ['0', '7', 'X', '0', '7', 'X', '0', '7', 'X'],
        ['7', 'X', '0', '7', 'X', '0', '7', 'X', '0']
    ]
    try:
        while True:
            print('1. Para jugar')
            print('2. Para salir')
            opcion = input('Ingrese la opcion: ')
            if opcion == '1':
                numeros = crear_numeros(3)
                resultado = mover_rodillo(rodillos, numeros)
                print('\nResultado: ')
                print(f'\n{rodillos[0][0]} - {rodillos[1][0]} - {rodillos[2][0]}\n')
                if ganar(resultado) and resultado[0][0] == 'X':
                    print('Ganaste 10 fichas')
                elif ganar(resultado) and resultado[0][0] == '0':
                    print('Ganaste 100 fichas')
                elif ganar(resultado) and resultado[0][0] == '7':
                    print('Ganaste 1000 fichas')
                else:
                    print("Perdiste, vuelve a intentarlo")
            elif opcion == '2':
                break
            else:
                print('Ingrese una opcion valida')
    except Exception as e:
        print(f'Ocurrio un error: {e}')

if __name__ == '__main__':
    jugar()


