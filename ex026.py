frase = str(input('Digite uma frase:')).strip()
m = frase.lower()
a1 = m.count('a') + m.count('â') + m.count('ã')
b = m.find('a')
bf = b + 1
c = m.rfind('a')
cf = c + 1
print ('''A letra A aparece {} vezes na frase 
A primeira letra A apareceu na posição {}
A última letra A apareceu na posição {}'''.format(a1, bf, cf))


