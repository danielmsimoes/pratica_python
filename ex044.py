import time

print('''============BOLA 7============''')
print('Atendimento...')
p = int (input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
time.sleep(0.3)
print ('[ 1 ] à vista dinheiro/cheque')
time.sleep(0.3)
print ('[ 2 ] à vista cartão')
time.sleep(0.3)
print ('[ 3 ] 2x no cartão')
time.sleep(0.3)
print ('[ 4 ] 3x ou mais no cartão')
op = (input('Qual opção de pagamento ?'))

if op == '1':
    r = 10 * p
    r1 = r / 100
    print ('Pagando em dinheiro/cheque você terá 10 % de desconto')
    print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, r1))

elif op == '2':
    r = 5 * p
    r1 = r / 100
    print ('Pagando em dinheiro/cheque você terá 5 % de desconto')
    print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, r1))


elif op == '3':
    r1 = p / 2
    print ('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(r1))
    print ('Sua compra não sofrerá alterações vai custar {:.2f} no final'.format(p))

elif op == '4':
    r = int (input('Quantas parcelas ?'))
    r1 = 20 * p
    r2 = (r1 / 100) + p
    r3 = r2 / r
    print ('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(r, r3))
    print ('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(p, r2 ))

else:
    aviso = 'OPÇÃO INVÁLIDA'
    print('{}{}{}, confira se a opção está correta'.format('\033[4;31m', aviso, '\033[m'))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, p))






