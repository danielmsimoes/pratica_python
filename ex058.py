import random
num = random.randint(0,10)
t1 = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi ?''')
acertou = False
while not acertou:
    palpite = int(input('Qual é o seu palpite ?'))
    if palpite != num:
        t1 +=1
    if palpite > num:
        print('Menos... Tente novamente')
    elif palpite < num:
        print('Mais... Tente novamente')
    if palpite == num:
        acertou = True

print(f'Acertou com {t1 + 1} tentativas. Parabéns')








