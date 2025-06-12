from datetime import date
y = int(input('Que ano quer analisar ? Coloque 0 para analisar o ano atual:'))
if y == 0:
    y = date.today().year
n = y % 4
if n == 0 and 100 % y != 0  or y % 400 == 0:
    print('O ano {} é BISSEXTO'.format(y))
else:
    print('O ano {} não é um ano BISSEXTO'.format(y))