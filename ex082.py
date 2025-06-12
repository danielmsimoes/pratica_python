# lista
lista = []
listap = []
listai = []
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    res = str(input('Quer continuar? [S/N]')).capitalize()
    if v % 2 == 0:
        listap.append(v)
    else:
        listai.append(v)
    if res == 'N':
        break
print(f'A lista completa {lista}')
# pares
print(f'A lista de pares é {listap}')
# impares
print(f'A lista de ímpares é {listai}')
