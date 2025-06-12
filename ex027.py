frase = str(input('Digite seu nome completo:')).strip()
f1 = frase.find(' ')
f2 = frase [0:f1]
f3 = frase.rfind(' ')
f4 = frase [f3:100]
print ('''Prazer em te conhecer!
Seu primeiro nome é {}
Seu último nome é {}'''.format(f2, f4))