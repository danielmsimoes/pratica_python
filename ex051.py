print('10 TERMOS DE UMA PA')
print('='*20)
t = int(input('Primeiro termo:')) #termo onde começa nossa progressão aritimética
r = int(input('Razão:')) #o espaço entre os números da PA
d = t + (10-1) * r    #esse é até aonde essa PA deve chegar para alcançar os primeiros 10 termos
for c in range (t,d + r , r): #usamos esse (d + r) pois ele sempre conta um número antes
    print (f'{c} ', end='→ ')
print('Acabou')

