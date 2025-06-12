somaidade = 0
media = 0
idade = 0
velho = 0
mulherq = 0
for c in range(1,5):

    print(f'----- {c}° PESSOA -----')
    n = str(input('Nome:')).capitalize()
    i = int(input('Idade:'))
    s = str(input('Sexo [M/F]:')).upper()
    somaidade += i
    if s == 'M' and idade < i:
        velho = i
        nomev = n
        tc = (f'O homem mais velho tem {velho} anos e se chama {nomev}')
    if s == 'F' and i < 20:
        mulherq += 1

media = somaidade / 4
print (f'A média de idade do grupo é de {media} anos')
print(f'{tc}')
print (f'Ao todo são {mulherq} mulheres com menos de 20 anos')


