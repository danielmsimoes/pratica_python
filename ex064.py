# num = num1 = 0 DICA
num = 0
num1 = 0
cont = -1
while num != 999:
    num1 += num
    num = int(input('Digite um número  [999 para parar]'))
    cont += 1
print(f'Você digitou {cont} e a soma entre eles foi {num1}.')
