cont = 0
num = int(input('Digite um número:'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'vermelho': '\033[31m'}
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        cont = cont + 1
    else:
        print('\033[31m', end='')
    print('{}{} '.format(c,cores['limpa']), end='')
if cont == 2:
    b = ('E por isso ele é um NÚMERO PRIMO!\033[m')
else:
    b = ('E é por isso que ele NÃO é um NÚMERO PRIMO!\033[m')
print('\nO número {} foi divisível {} vezes '.format(num,cont))
print(b)