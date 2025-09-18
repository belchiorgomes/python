numeros = [1, 2, 3, 4, 5]
# novos_numeros = [numero for numero in numeros]
# print(numeros)
# print(novos_numeros)

# Esse codigo de cima e mais facil de escrever do que esse de baixo, e eles fazem a mesma coisa

# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)
# print(novos_numeros)

def divisaoFn(x,y):
    return x / y

# divisao = [numero / 2 for numero in numeros]
divisao = [divisaoFn(numero, 2) for numero in numeros]
print(divisao)