import math
# round the number
a = float (input('Digite o ângulo que você deseja:'))
ra = math.radians(a)
s = math.sin(ra)
c = math.cos(ra)
t = math.tan(ra)
print ('O ângulo de {} tem o SENO de {:.2f} \nO ângulo de {} tem o COSSENO de {:.2f}\n'.format (a, s, a, c), end='')
print ('O ângulo de {} tem a TANGENTE de {:.2f}'.format (a, t))