p1 = {
    'nome': 'Breno',
    'idade': 31,
}

print(p1)
# print(p1.get('nome'))

p1.update({
    'nome': 'Julia',
    'altura': 1.69
})

print(p1)

p1.update(nome='Rafaela', cidade='Qualquer cidade')

for chave in p1:
    print(chave, p1.get(chave))
    # print(f'{chave} {p1.get(chave)}')  