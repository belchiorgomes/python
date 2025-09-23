import sys

generator = (n for n in range(1, 1000))
lista = [n for n in range(1, 1000)]
print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

generator1 = (n for n in range(1, 11))
for n in generator1:
    print(n)