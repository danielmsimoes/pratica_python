import time
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('Vamos jogar um jogo ?')
print('''Suas opções são essas:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
erro = 'JOGADA INVÁLIDA'
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'vermelho':'\033[31m'}
jogador = int(input('Qual é a sua jogada ?'))
if jogador >= 3:
     print('{}{}{}, verifique se está correta a opção.'.format(cores['vermelho'], erro, cores['limpa']))
     exit()
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('-=-' * 10)
print('Jogador jogou {}'.format(jogador))
print('Computador jogou {}'.format(itens[pc]))
print('-=-' * 10)
if pc == 0 : #pc jogou pedra
     if jogador == 0:
          print('EMPATE')
     elif jogador == 1:
          print('VOCÊ VENCEU!')
     elif jogador == 2:
          print('O COMPUTADOR VENCEU')
     else:
          print('{}{}{}, verifique se está correta a opção'.format(cores['vermelho'], erro, cores['limpa']))
elif pc == 1 : #pc jogou Papel
     if jogador == 0:
          print('O COMPUTADOR VENCEU')
     elif jogador == 1:
          print('EMPATE')
     elif jogador == 2:
          print('VOCÊ VENCEU!')
     else:
          print('{}{}{}, verifique se está correta a opção'.format(cores['vermelho'], erro, cores['limpa']))
elif pc == 2: #pc jogou tesoura
     if jogador == 0:
          print('VOCÊ VENCEU!')
     elif jogador == 1:
          print('O COMPUTADOR VENCEU')
     elif jogador == 2:
          print('EMPATE')
     else:
          print('{}{}{}, verifique se está correta a opção'.format(cores['vermelho'], erro, cores['limpa']))


