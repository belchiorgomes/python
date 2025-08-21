frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
print(lista_palavras)

lista_palavras = frase.split(', ')
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())

for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()
    print(lista_palavras)

frases_unidas = ' - '.join(lista_palavras)
print(frases_unidas)

print('---------------------------')

salas = [
    ['Maria','Eduarda',],
    ['Henena',],
    ['Maria Vitoria', 'Priscila', 'Julia',],
]

print(salas)