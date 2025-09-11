pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Cristina',
}

outros_dados = {
    'idade': 30,
    'altura': 1.68,
}

pessoa_completa = {**pessoa}
print(pessoa_completa)

pessoa_completa = {**pessoa, **outros_dados}
print(pessoa_completa)

pessoa_completa = {**pessoa, 'chave': 1}
print(pessoa_completa)

def mostra_argumentos_nomeados(*ars, **kwargs):
    print(kwargs)

mostra_argumentos_nomeados(nome='Julia', idade=23, chave=123)