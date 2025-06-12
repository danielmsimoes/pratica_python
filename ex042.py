# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes
print ('-=-' * 10)
print ('ANALISADOR DE TRIÂNGULOS')
print ('-=-' * 10)
a = float(input('Primeiro seguimento:'))
b = float(input('Segundo seguimento:'))
c = float(input('Terceiro seguimento:'))
if a + b > c and b + c > a and a + c > b:
    print('Os seguimentos acima PODEM FORMAR um triângulo')
    if a == b == c:
        print ('Um EQUILÁTERO')
#!= (diferente de)
    if a == b != c or a == c != b or b == c != a:
        print ('Um ISÓCELES')
    if a != b != c and a != b != c and b != c != a:
        print ('Um ESCALENO')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo')

