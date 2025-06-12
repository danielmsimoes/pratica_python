conti = conth = contm = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    i = int(input('Idade:'))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F]')).upper().strip()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if s == 'f' and i > 20:
        contm += 1
    if i > 18:
        conti += 1
    if s == 'M':
        conth += 1
    if continuar == 'N':
        break

print(f'''Total de pessoas com mais de 18: {conti}'
      Ao todo temos {conth} homens cadastrados
      E temos {contm} mulheres com menos de 20 anos''')


