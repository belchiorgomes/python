nome = input('Digite um nome! ')

tamanho_nome = len(nome)

x = 0
novo_nome = ' '
while x < tamanho_nome:
    letra = nome[x]
    novo_nome += f'#{letra}'
    x += 1
print(novo_nome)
print('FIM')