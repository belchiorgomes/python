contador = 0

while contador <= 100:
    contador += 1

    if contador >= 8 and contador <= 12:
        # print('Nao vou mostrar o numero 8')
        continue

    if contador == 40:
        break

    print(contador)
print('Fim do Programa!')