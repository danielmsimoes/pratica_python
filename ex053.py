frase = (input('Digite uma frase:')).upper()
f = frase.split()
f1 = ''.join(f)
inverso = ''
for c in range (len(f1)-1, -1, -1):
    inverso += f1[c]
if inverso == f1:
    print(f'O inverso de {f1} é {inverso}')
    print('Temos um palíndromo')
else:
    print(f'O inverso de {f1} é {inverso}')
    print ('A frase digitada não é um palíndromo')
