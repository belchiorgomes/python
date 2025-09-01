a = 1

def escopo():
    def nova_funcao(b=3):
        print(a, b, sep=' - ')
    nova_funcao()
    print(a)

escopo()