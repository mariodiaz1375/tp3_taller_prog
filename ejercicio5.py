from ejercicio1 import ingresar_numero, ingresar_numero_entero

def desplegar_menu():
    try:
        while True:
            print('1. Calcular potencia')
            print('2. Obtener los digitos de un numero')
            print('3. Comprobar si un numero es capicua')
            print('4. Salir')
            opcion = input('Ingrese una opcion: ')

            if opcion == '1':

                print('\nIngrese la base')
                base = ingresar_numero()
                print('Ingrese el exponente')
                exponente = ingresar_numero_entero()
                resultado = calcular_potencia(base, exponente)
                print(f'El resultado de la potencia es: {resultado}\n')

            elif opcion == '2':
                
                print('\nIngrese el numero')
                numero = ingresar_numero_entero()
                digitos = contar_digitos(numero)
                print(f'El numero {numero} tiene {digitos} digitos\n')

            elif opcion == '4':
                break

            else:
                print('Ingrese una opcion valida')
    except Exception as e:
        print(f'Ocurrio un error: {e}')


def calcular_potencia(num, ex):
    return num**ex

def contar_digitos(num):
    num = str(num)
    return len(num)

def det_capicua(num):
    num = str(num)
    if num == num.reverse():
        return True
    else:
        return False
    

if __name__ == '__main__':
    print('Ejercicio 5')
    desplegar_menu()



