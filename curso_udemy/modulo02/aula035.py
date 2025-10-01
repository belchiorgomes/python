# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import sys

import aula035_m
from aula035_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print(*sys.path, sep='\n')

print(aula035_m.soma(2, 3))
print(soma(2, 3))

print(aula035_m.variavel_modulo)
print(variavel_modulo)