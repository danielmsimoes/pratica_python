from random import randint
r1 = cont = 0
print('-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*10)
while True:
    valor = int(input('Diga um valor:'))
    pi = str(input('Par ou Ímpar? [P/I]')).upper()
    pc = randint(0, 10)
    soma = valor + pc
    r = soma % 2
    if r == 0:
        r1 = 'DEU PAR'
        pi1 = 'P'
    else:
        r1 = 'DEU ÍMPAR'
        pi1 = 'I'
    print(f'Você jogou {valor} e o computador {pc}. Total de {soma} {r1} ')
    if pi1 == pi:
        print('Você VENCEU!')
        cont += 1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {cont} vezes.')


# n1 = int(input('valor'))
# n2 = int(input('valor'))
# n3 = n1 + n2
# pi = n3 % 2
# print(n3)
# print(pi)











# error
# while pi not in 'PI':
#     print('Dados inválidos, tente novamente.')
#     break hb