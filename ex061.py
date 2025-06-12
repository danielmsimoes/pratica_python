print ('Gerador de PA')
print ('-=-'*10)
t = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
termo = t 
cont = 1
while cont <= 10:
    print(f'{termo}', end=' → ')
    termo += razao
    cont += 1
print('FIM')

