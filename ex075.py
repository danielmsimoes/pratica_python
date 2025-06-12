supla = (int(input('Digite um número:'))), int(input('Digite outro número:')), int(input('Digite mais um número:')), int(input('Digite o último número:'))
print(f'Você digitou os valores {supla}')
countn = supla.count(9)
loc = supla.index(3)
print(f'O valor 9 apareceu {countn} vezes')
if 3 in supla:
    print(f'O valor 3 apareceu na {loc +1} posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram', end=': ')
for n in supla:
    a = n % 2
    if a == 0:
        print(f'{n}  ', end=' ')