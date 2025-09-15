lista = [n for n in range(10) if n < 5]
print(lista)
print()

# lista2 = []
# for x in range(3):
#     for y in range(3):
#         lista2.append((x,y))
# print(lista2)

lista2 = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
print(lista2)