frase = 'O Python é uma lingugem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum.'.lower()

# print(frase.count('python'))

indice = 0
while indice < len(frase):
    letra_atual = frase[indice]

    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    print(f'{letra_atual} = {quantas_vezes_letra_apareceu}')
    indice += 1
print('FIM')