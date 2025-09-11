a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

# print(pessoa)
a, b = pessoa
print(a, b)

a, b = pessoa.values()
print(a, b)

for chave, valor in pessoa.items():
    print(chave, valor)