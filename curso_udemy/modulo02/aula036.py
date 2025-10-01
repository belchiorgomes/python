# import aula036_m

# print(aula036_m.nome)

# for i in range(10):
#     # print(i)
#     import aula036_m

# print('FIM')

import importlib
import aula036_m

for i in range(1, 11):
    importlib.reload(aula036_m)
    print(i)
print('FIM')