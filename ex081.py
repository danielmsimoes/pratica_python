lista = []
cont = 0
while True:
    v = int(input('Digite um valor:'))
    lista.append(v)
    cont += 1
    resp = str(input('Quer continuar? [S/N]')).capitalize()
    if resp == 'N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')