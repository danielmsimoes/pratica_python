s = int(input('Qual é o salário do funcionário? R$ '))
if s > 1250:
    sf = s + (s * 10 /100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s, sf))
if s <= 1250:
    sf = s + (s * 15 /100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s, sf))