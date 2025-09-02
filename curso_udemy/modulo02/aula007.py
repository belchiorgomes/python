# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args):
    total_multi = 1
    for numeros in args:
        total_multi *= numeros
    return total_multi
numeros_multiplicacao = multiplicacao(2, 3, 5)
print(numeros_multiplicacao)

print('----------------------')

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

"""def par_impar(*args):
    for numero in args:
        # print(numero)/
        if numero % 2 == 0:
            print(f'O numero {numero} é PAR')
        else:
            print(f'O numero {numero} é IMPAR')
par_impar(10, 3, 4, 11, 1, 500)"""

def par_impar(*args):
    for numeros in args:
        multiplo_2 = numeros % 2 == 0

        if multiplo_2:
            print(f'O numero {numeros} é PAR')
        else:
            print(f'O numero {numeros} é IMPAR')
par_impar(1, 4, 10)