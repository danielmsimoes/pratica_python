'''ca = float(input ('Qual é o valor do cateto adjacente:'))
co = float(input ('Qual é o valor do cateto oposto: '))
hip = (ca ** 2 + co ** 2) ** (1/2)
print ('A hipotenusa vai medir {:.2f}'.format (hip))'''
import math
ca = float(input ('Qual é o valor do cateto adjacente:'))
co = float(input ('Qual é o valor do cateto oposto: '))
hip = math.hypot(ca, co)
print ('O valor da hipotenusa é : {:.2f}'.format (hip))
