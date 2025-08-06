entrada = input('Digite a hora em números inteiro: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom Dia')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa Noite')
    else:
        print('Esse horario não e valido')
except:
    print('Nao foi informado um horario correto')