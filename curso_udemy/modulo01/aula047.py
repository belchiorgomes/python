# nomes = ['Maria', 'Helena', "Luiza"]
# nome1, nome2, nome3 = nomes

# nome1, nome2, nome3 = ['Maria', 'Helena', "Luiza"]

nome1, *_ = ['Maria', 'Helena', "Luiza"]
print(nome1, _)

#------------------------------------------------
print('----------------------------------------')

lista = [123, "Maria Vitoria", 12.2, True]
lista_enumerada = enumerate(lista)
print(f'{lista}\n')
print(lista_enumerada)

for item in lista_enumerada:
    print(item)

#-------------------------------
print('----------------------------------------')

nomes = ['Ana Vitoria', 'Maria Vitoria', 'Maria Tereza']
for indice, nome in enumerate(nomes):
    print(indice,nome)