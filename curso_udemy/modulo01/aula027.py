numero = input('Por favor, digite um numero inteiro? ')

if numero.isdigit():
    numero_int = int(numero)
    print('Você digitou um numero inteiro')
    if numero_int % 2 == 0:
        print(f'O numero digitado {numero_int} é par')
    else:
        print(f'O numero digitado {numero_int} é impar')
else:
    print('Você não digitou um numero inteiro')