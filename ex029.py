v =  float(input('Qual é a velocidade atual do carro ? '))
if v > 80:
    s = (v - 80) * 7
    print('''MULTADO! Você excedeu o limite permitido que é de 80Km/h
    Você deve pagar uma multa de R${:.2f}!'''.format(s))
else:
    print('Tenha um bom dia ! Dirija com segurança!')