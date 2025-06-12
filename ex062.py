print('Gerador de PA')
print('-=-'*10)
t = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
cont = 0
termo = t
repetir = 9
# equacao = termo + (10-1) * razao
while cont <= repetir:
    print(f'{termo}', end=' → ')
    cont += 1
    termo += razao
repetir1 = 1
print('PAUSA')
while repetir1 != 0:
    repetir1 = int(input('Quantos termos você quer mostrar a mais ?'))
    repetir += repetir1

    while cont <= repetir:
        print(f'{termo}', end=' → ')
        termo += razao
        cont += 1
    print('PAUSA')
print(f'Progressão finalizada com {cont} termos mostrados.')

