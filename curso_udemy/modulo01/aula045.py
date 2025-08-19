lista = [10, 20, 30, 40]
# lista.append('Breno')
# nome = lista.pop()
# print(lista, nome)

lista.insert(0, 5)#insere elemento na lista
print(lista)
print(lista[3])

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_c)
print(lista_d)

lista_e = ['Breno', 'Rafaela']
lista_f = lista_e.copy()

# lista_f = lista_e
# print(lista_e)
lista_e[1] = 'Ana Vitoria'
print(lista_e)

print(lista_f)