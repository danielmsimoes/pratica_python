cores = {'limpa': '\033[m',
         'vermelho': '\033[31m'}


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break
        else:
            print('{}ERRO! Digite um número inteiro válido.{}'.format(cores['vermelho'], cores['limpa']))
        if ok:
            break
    return valor

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar um número {n}')
