continuar = 'sim'

while continuar.lower() != 'nao':
    try:
        numero1 = float(input('Digite um numero '))
        numero2 = float(input('Digite outro numero '))

        soma = numero1 + numero2
        print(f'A soma entre {numero1} + {numero2} = {soma} \n')

        continuar = str(input('Digite (SIM) para continuar ou (NÃO) para finalizar o programa '))

        if continuar != 'sim' or continuar != 'nao':
            print('Você digitou outra coisa sem ser sim ou não')
            continue

    except ValueError:
        print('Digite apenas numero')
    # except Exception:
    #     print('Outro erro')
print('Programa encerrado com sucesso.')