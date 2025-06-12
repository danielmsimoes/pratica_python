n = (input('Digite seu nome completo:'))
#maiusculo
u = n.upper()
#minusculo
l = n.lower()
#letras
nl = n.strip
all = len(n)
esp = n.count(' ')
rf = all - esp
#primeiro nome
ni = n.split()
ne = ni [0]
nf = len(ne)
print ('''Analisando seu nome...
Seu nome em maiúsculas é {}
Seu nome em minúsculas é {}
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras '''.format(u, l, rf, ne, nf))

