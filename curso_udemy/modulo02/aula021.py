# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

print(list(range(10)))
print()

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)
print()

#List comprehension em Python
lista2 = [numero + numero for numero in range(5)]
print(lista2)