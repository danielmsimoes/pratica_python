from uteis import numeros

num = int(input('DIgite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O dobro de {num} é {numeros.triplo(num)}')