continuar = 'sim'

while continuar.lower() != 'nao':
    try:
        numero1 = float(input('Digite um numero '))
        numero2 = float(input('Digite outro numero '))

        soma = numero1 + numero2
        print(f'A soma entre {numero1} + {numero2} = {soma} \n')

        validacao_resposta = True
        while validacao_resposta:
            resosta = str(input('Deseja fazer outra soma (SIM/NÃO) \n'))

            if resosta.lower() == 'sim':
                continuar = 'sim'
                validacao_resposta = False

            elif resosta.lower() == 'nao':
                continuar = 'nao'
                validacao_resposta = False

            else:
                print('Resposta inválida. digite "sim" ou "nao" \n')

    except ValueError:
        print('Digite apenas numero')

print('Programa encerrado com sucesso.')