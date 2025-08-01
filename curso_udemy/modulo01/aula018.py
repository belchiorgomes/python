primeiro_valor = int(input('Digite o primeiro valor '))
segundo_valor = int(input('Digite o segundo valor '))

print(f'Primeiro valor: {primeiro_valor} \n Segundo valor: {segundo_valor}')

if primeiro_valor > segundo_valor:
    print('Primeiro valor e maior')
elif primeiro_valor < segundo_valor:
    print('Segundo valor maior')
elif primeiro_valor == segundo_valor:
    print('Os dois valores sao iguais')
else:
    print('Não foi digitado valor numerico')