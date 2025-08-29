def nova_funcao():
    print('Cria uma nova função')

nova_funcao()

def soma_numeros(a, b):
    a + b

print(soma_numeros(2, 3))

def saudacao(nome):
    print(f'Ola {nome}')

saudacao('Breno Gomes')

def saudacao_sem_nome(nome='Não tem nome'):
    print(f'Ola {nome}')

saudacao_sem_nome('Maria')
saudacao_sem_nome()