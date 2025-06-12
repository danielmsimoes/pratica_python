from random import randint
from time import sleep
lista = []
olista = []
a = 'JOGA NA MEGA SENA'
print('-'*30)
print(f'{a:^30}')
print('-'*30)
jogos = int(input('Quantos jogos você quer que eu sorteie?'))
tot = 1
while tot <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    olista.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3,  f' SORTEANDO {jogos} JOGOS ',  '-='*3)
print()
for i, l in enumerate(olista):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('-='*3,  f' BOA SORTE!',  '-='*3)