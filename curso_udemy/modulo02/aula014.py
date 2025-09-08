# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados
print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s2 = {1, 2, 3, 3, 3, 3, 3, 1}
print(s2) #remove os valores duplicados

l1 = {1, 2, 3, 3, 3, 3, 3, 1}
s3 = set(l1)
l2 = list(s3)
print(l2)

s4 = set('Breno')
print(s4)
print('r' in s4) #mostra um valor Bool 'se a letra r tiver no'
                 #set s4 vai ser True


# Métodos úteis:
# add, update, clear, discard

s5 = set()
s5.add('Breno')
s5.add(1)
s5.update(('Olá, Mundo', 1, 2, 3))
print(s5)
s5.discard('Olá, Mundo')
print(s5)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s6 = {1, 2, 3}
s7 = {2, 3, 4}

s8 = s6 | s7
print(s8)

s8 = s6 & s7
print(s8)

s8 = s6 - s7
print(s8)

s8 = s6 ^ s7
print(s8)