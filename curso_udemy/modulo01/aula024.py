"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome} \n e sua idade é {idade}')
    print(f'\n O seu nome invertido fica {nome[::-1]} \n')
    print(f'{nome} tem {len(nome)} caracteres.')
    print(f'Primeira letra do seu nome é {nome[0]}, e a ultima é {nome[-1]}')

    if " " not in nome:
        print(f'Seu nome nao contem espaço')
    else:
        print(f'Seu nome contem espaços')
else:
    print('Desculpe faltou campos a ser digitados!')
