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

def nada():
    pass

if __name__ == '__main__':
    texto = 'La seguridad es una competencia'
    print(texto)
    print(f'Cantidad de vocales: {contar_vocales(texto)}')
    print(f'Cantidad de consonantes: {contar_consonantes(texto)}')

