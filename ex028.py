import random
import time

c = int(input('''Vou pensar em um número de 0 á 5. Tente advinhar...
Em que número eu pensei ?'''))
ak = random.randint(0,5)
print('PROCESSANDO...')
time.sleep(1)
if c > 5:
    print ('''Este número está fora dos padrões.
    Veja novamente se digitou um número entre 0 á 5''')
    exit()
if c == ak:
    print ('PARABÉNS, você me superou!')
else:
    print ('GANHEI!, eu pensei no {} e não no {}!'.format(ak,c))
