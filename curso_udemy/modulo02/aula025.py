# for x in range(1, 6):
#     for y in range(1, 4):
#         print(x,y)

linha_colunas = [
    {x, y}
    for x in range(1, 6)
    for y in range(1, 4)
]
print(linha_colunas)