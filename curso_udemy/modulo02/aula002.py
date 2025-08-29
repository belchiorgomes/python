def multiplo(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de {multiplo} ', end='')
    print(resultado)

multiplo(16, 8)
multiplo(15, 3)
multiplo(10, 2)