cont = 0
soma = 0
for c in range (1, 7):
    v = int(input(f'Digite o {c} valor:'))
    if v % 2 == 0:
        soma = soma + v
        cont = cont + 1
print (f'Você informou {cont} números PARES e a soma foi {soma}')