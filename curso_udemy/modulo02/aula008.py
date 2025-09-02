"""
Closure e funções que retornam outras funções
"""

"""
def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('Bom Dia', 'Breno')
s2 = criar_saudacao('Bom Noite', 'Ana')
print(s1())
print(s2())
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom Dia')
falar_boa_noite = criar_saudacao('Boa Noite')

for nome in ['Ana Maria', 'Jaqueline', 'Roberto', 'Janaina']:
    print(falar_bom_dia(nome))