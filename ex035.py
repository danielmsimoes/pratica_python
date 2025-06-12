print ('-=-' * 10)
print ('ANALISADOR DE TRIÂNGULOS')
print ('-=-' * 10)
a = float(input('Primeiro seguimento:'))
b = float(input('Segundo seguimento:'))
c = float(input('Terceiro seguimento:'))
if a + b > c and b + c > a and a + c > b:
    print('Os seguimentos acima PODEM FORMAR um triângulo')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo')