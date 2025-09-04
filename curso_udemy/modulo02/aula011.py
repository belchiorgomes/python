pessoa = {}

recebe_nome = input('Digite seu nome ')
recebe_idade = input('Digite sua idade ')
# recebe_altura = input('Digite sua altura ')


chave_nome = 'nome'
chave_idade = 'idade'
pessoa[chave_nome] = recebe_nome
pessoa[chave_idade] = recebe_idade

for chaves in pessoa:
    print(chaves, pessoa[chaves])

print(f'Esse dicionario tem {len(pessoa)} itens')

print(tuple(pessoa.keys()))
print(tuple(pessoa.values()))

# print(pessoa)
# print(pessoa[chave])