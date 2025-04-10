pacientes = ['adan tolaba', 'morales alejandro', 'Daniel Garcia']

def desplegar_menu():
    try:
        while True:
            print('\n1. Agregar un paciente')
            print('2. Atender paciente')
            print('3. Mostrar los pacientes que faltan ser atendidios')
            print('4. Salir')
            opcion = input('Ingrese una opcion: ')

            if opcion == '1':
                paciente = input('Ingrese el nombre del paciente: ')
                urgencia = input('El paciente es de urgencia?: ')
                if urgencia.lower() == 'si':
                    pacientes.insert(0, paciente)
                else:
                    pacientes.append(paciente)

            elif opcion == '2':

                paciente = pacientes[0].upper()
                print(f'\nSe atendera al siguiente paciente de la lista: {paciente}')
                pacientes.pop(0)
                print(f'Se atendio al paciente: {paciente}')
                print(f'Siguiente paciente de la lista: {pacientes[0].upper()}')

            elif opcion == '3':

                cantidad = len(pacientes)
                print(f'\nQuedan {cantidad} pacientes por ser atendidos: ')
                for paciente in pacientes:
                    print(paciente.upper())
                

            elif opcion == '4':
                break

            else:
                print('Ingrese una opcion valida')
    except Exception as e:
        print(f'Ocurrio un error: {e}')

if __name__ == '__main__':
    desplegar_menu()