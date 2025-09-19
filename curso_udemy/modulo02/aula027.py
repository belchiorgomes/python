# Dicionario em python
produtos = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'Categoria': 'Escritório',
}

for chave, valor in produtos.items():
    print(chave, valor)

print()
print(produtos.items(), '\n')
print(produtos['nome'], produtos['preco'], '\n')

novo_produtos = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produtos.items()
    # if chave != 'categoria'
}
print(novo_produtos)