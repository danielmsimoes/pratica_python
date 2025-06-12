from random import randint
maior = 0
menor = 11
lista = (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10))
# if lista[0] > lista[1]:
print('Os valores sorteados foram: ', end='')
for n in lista:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(lista)}')
print(f'O menor valor sorteado foi {min(lista)}')



