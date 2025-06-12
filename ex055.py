from datetime import date
maior = 0
menor = 999999999
for c in range (1,6):
    peso = float(input(f'Peso da {c}° pessoa:'))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print (f'O maior peso lido foi {maior}kg.')
print (f'O menor peso lido foi {menor}kg.')
