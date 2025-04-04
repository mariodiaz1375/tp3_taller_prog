def contar_vocales(palabra):
    contador = 0
    for letra in palabra:
        if letra.lower() in 'aeiouáéíóú':
            contador += 1
    return contador

def contar_consonantes(palabra):
    contador = 0
    for letra in palabra:
        if letra.lower() in 'bcdfghjklmnpqrstvwyz':
            contador += 1
    return contador

if __name__ == '__main__':
    oracion = 'La seguridad es una competencia'
    print(f'Cantidad de vocales: {contar_vocales(oracion)}')
    print(f'Cantidad de consonantes: {contar_consonantes(oracion)}')

