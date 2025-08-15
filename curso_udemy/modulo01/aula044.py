"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# numero_lista = lista[2]
# print(numero_lista)

lista[2] = 300
print(lista)
del lista[2]
print(lista)

lista.append(50)
print(lista)
ultimo_valor_removido = lista.pop()
print(f'Ultimo valor removido foi {ultimo_valor_removido}')
lista.append(60)
lista.append(70)
print(lista)