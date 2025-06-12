print('='*30)
print('{:^30}'.format('BANCO DAN'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
while True:
    dic = valor // 50
    resto = valor % 50
    print(f'Total de {dic} cédulas de R$50')
    if resto >= 20:
        div = resto // 20
        resto1 = resto % 20
        print(f'Total de {div} cédulas de R$20')
    else:
        resto1 = resto
    if resto1 >= 10:
        did = resto1 // 10
        resto2 = resto1 % 10
        print(f'Total de {did} cédulas de R$10')
    else:
        resto2 = resto1
    if resto2 < 10 and resto2 > 0:
        diu = resto2 // 1
        resto3 = resto2 % 1
        print(f'Total de {diu} cédulas de R$1')
    else:
        resto3 = resto2
    if resto3 == 0:
        break
print('='*20)
print('Volte sempre ao BANCO DAN! Tenha um ótimo dia!')

