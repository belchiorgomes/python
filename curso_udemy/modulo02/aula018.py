def executa(funcao, *args):
    return funcao(*args)

def soma(a, b):
    return a + b

resultado = executa(soma, 10, 5)
print(resultado)  # 15


def saudar(nome='Julia'):
    return f'olà prazer em conhecelo {nome}'

saudacao1 = executa(saudar, 'Breno')
saudacao2 = executa(saudar, )
print(saudacao1)
print(saudacao2)

# def soma(x, y):
#     return x + y

#esses treis prints são a mesma coisa
print(executa(lambda x, y: x + y, 2, 3))
print(executa(soma, 3, 4))
print(soma(5, 5))