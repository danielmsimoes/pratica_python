n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1**n2
print ('A soma é {} \n A multiplicação é {} \n A divisão é {}'.format (s, m, d,), end=',')
print (' A divisão inteira é {} \n A potênciação {}'.format (di, p))