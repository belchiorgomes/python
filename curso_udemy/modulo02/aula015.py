# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Você digitou as seguintes letras: ', letras)
        print('Parabens! a letra era ', letra)
        break

    print(letras)