numeros = [numero + 1 for numero in range(10)]
print(numeros)

numeros1 = [numero for numero in range(10) if numero > 5]
print(numeros1)

numeros_impares = [numero for numero in range(10) if numero % 2 != 0]
print(f'Os numeros impares são {numeros_impares}')

diferenca_numero = [
        numero
        if numero != 6 
        else 600
        for numero in range(10)
    ]
print(diferenca_numero)