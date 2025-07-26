numeros = [1, 2, 3, 4, 5]

print(numeros)

numeros.append(6)#ADICIONA UM VALOR A LISTA
print(numeros)

numeros.insert(0, 0)#INSERE O NUMERO 0 NO INDICE 0 (PRIMEIRO VALOR = INDICE, SEGUNDO VALOR = VALOR DA LISTA)
print(numeros)

nomes = ['Barbara', 'Vanessa']
idades = [31, 28]

nomes.extend(idades)#METODO QUE JUNTA AS DUAS LISTAS EM UMA UNICA
print(nomes)