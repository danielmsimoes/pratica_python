from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for num in range(0, 5):
        n = randint(0, 9)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar (lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando so valores pares de {numeros}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
print(numeros)
