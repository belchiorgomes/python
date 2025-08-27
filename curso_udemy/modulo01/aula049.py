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
    ['Maria', 'Eduarda', ],
    ['Helena', ],
    ['Maria Vitoria', 'Priscila', 'Julia', (0, 10, 20, 30, 40)],
]

print(salas)
print(salas[1])
print(salas[2][1])
print(salas[2][3][3])

print('--------------------------------------')

salaAlunos = [
    ['Maria', 'Eduarda', ],
    ['Helena', ],
    ['Maria Vitoria', 'Priscila', 'Julia', ],
]

for sala in salaAlunos:
    print(f'A sala {sala}')
    for alunos in sala:
        print(alunos)