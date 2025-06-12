num = soma = cont = maior = 0
menor = 9999999999999999999999999999999999999999999999
continuar = str
while continuar != 'N':
    num = int(input('Digite um número:'))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    cont += 1
    media = soma / cont
    continuar = str(input('Quer continuar? [S/N]')).capitalize()
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')