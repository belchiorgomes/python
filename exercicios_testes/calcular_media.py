soma = 0
qdt_nota = 0
while True:
    try:
        nota = float(input('Digite uma nota (ou um numero negatiovo para sair) \n'))

        
        # if nota < 0:
        #     print('Nenhuma nota digitada \n')
        #     break
        # else:
        #     soma += nota
        #     qdt_nota += 1

        if nota >= 0:
            soma += nota
            qdt_nota += 1
        else:
            print('Nenhuma nota digitada \n')
            break

        media = soma / qdt_nota
    except ValueError:
        print('Por favor informe uma nota correta \n')

print(f'A soma entre as notas e {soma} \n')
print(f'A media entre as notas foi {media:.2f} \n')
print(f'Foi digitada {qdt_nota} notas \n')
print('Programa finalizado com sucesso! ')