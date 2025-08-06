"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True
while True:
    nome = input('Digite seu nome, ou digite sair, para finalizar o programa ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break
print('Programa finalizado com sucesso!')
