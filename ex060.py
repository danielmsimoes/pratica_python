num = int(input('Digite um número para'
                'calcular seu Fatorial:'))
num1 = num
f = 1
print(f'Calculando {num}! = ', end='')
while num1 > 0:
    print(f'{num1}', end='')
    print(' x ' if num1 > 1 else ' = ', end='')
    f *= num1
    num1 -= 1    # num1 = num1-1 variavel recebe ela mesmo menos 1
print (f'{f}')


