nomes = ['Ana Vitoria', 'Leticia', 'Carla']

print(nomes[1])#MOSTRA O ITEM 1 DA LISTA 'A LISTA COMEÇA NO ÍNDICE 0' ENTAO O NOME[1] = Leticia
print(nomes[-1])#NUMEROS NEGATIVOS COMEÇA A CONTAR NO ULTIMO ELEMENTO DA LISTA

comidas = ['Arroz', 'Feijao', 'Macarrao', 'Leite', 'Milho', 'estrado', 'Carnes']
indiceComida = comidas[1:4]#CRIA UMA FAIXA DE ÍNDICE PARA A CRIAÇÃO DE UMA NOVA LISTA
print(indiceComida)
print(comidas[:3])
print(comidas[4:])

if 'Leite' in comidas:
    print("Leite tem nessa lista de comidas")