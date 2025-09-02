x, y, *resto = 1, 2, 3, 4, [2, 6]
print(x, y, resto)

def soma(*args):
    for numeros in args:
        print(numeros)
    print(args, type(args))
soma(2,4,5,8,10)

print('------------------')

# def soma1(*args):
#     total = 0
#     for numero in args:
#         print('Total', total, numero)
#         total += numero
#         print('Total', total)
#     print(total)
# soma1(1,2,3,4,5)

def soma1(*args):
    total = 0
    for numeros in args:
        total += numeros
    return total

soma_valores = soma1(1,2,3)
print(soma_valores)