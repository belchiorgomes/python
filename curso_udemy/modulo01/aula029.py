primeiro_nome = input('Digite seu primeiro nome: ')

tamanho_nome = len(primeiro_nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome e curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')