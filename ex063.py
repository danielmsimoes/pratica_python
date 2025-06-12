print('---' * 10)
print('Frequência de Fibonacci')
print('---' * 10)
termo = int(input('Quantos termos você quer mostrar ?'))
num = 0
num1 = 1
print('~~~' * 30)
print(f'{num} → {num1}', end=' → ')
cont = 3
while cont <= termo:
    num2 = num + num1
    print(f'{num2}', end=' → ')
    num = num1
    num1 = num2
    cont += 1
print('FIM')
print('~~~' * 30)
