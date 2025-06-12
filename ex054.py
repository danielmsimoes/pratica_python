from datetime import date
cont = 0
cont1 = 0
for c in range (1,8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu ?'))
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        cont += 1
    else:
        cont1 += 1
print (f'Ao todo tivemos {cont} pessoas maiores de idade')
print (f'E também tivemos {cont1} pessoas menores de idade')


