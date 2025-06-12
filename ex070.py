pre = soma = contm = 0
menor = 99999999999999999999999999999999999
a = ('-'*20)
print (a)
print('SUPER BARATÃO')
print (a)
while True:
    pro = str(input('Produto:')).strip()
    pre = float(input('Preço:'))
    soma += pre
    if pre > 1000:
        contm += 1
    if pre < menor:
        menor = pre
        prom = pro
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if conti == 'N':
        break
print(f'{a} FIM DO PROGRAMA {a}')
print('''O total da compra foi R${:.2f}
Temos {} produto custando mais de R$1000.00
O produto mais barato foi {} que custa R${:.2f}'''.format(soma, contm, prom, menor))
