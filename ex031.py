km= int(input('Qual é a distância da sua viagem?'))
print('Você está preste a começar uma viagem de {}KM.'.format(km))
if km <= 200:
    km1 = km * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(km1))
else:
    km2 = km * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(km2))