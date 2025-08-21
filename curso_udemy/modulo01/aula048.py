lista_compra = []

while True:
    print('Selecione uma opção ')
    opcao = input('[i]nserir [a]pagar l[istar] ')

    if opcao == 'i' or opcao == 'a' or opcao == 'l':
        print('Oção valida ')

        # lista_compra = []

        if opcao == 'i':
            novo_item_lista = input('Digite qual item que você quer adicionar na sua lista: ')
            lista_compra.append(novo_item_lista)
            print('Item inserido com sucesso: ')

        elif opcao == 'a':
            print(f'Minha lista atual e: {lista_compra}')
            remover_item_lista = input('Selecione um item na lista a ser removido: ')

            try:
                lista_compra.remove(remover_item_lista)
                print(f'O item {remover_item_lista} foi removido com sucesso! ')
            except ValueError:
                print(f'Erro: o item {remover_item_lista} não foi encontrado na sua lista ')

        elif opcao == 'l':
            print(f'Sua lista de compras é {lista_compra}')
    else:
        print('opção invalida, selecione uma opção valida ')