pi = float(input('Qual o preço do produto:R$'))
pc = float (input ('Qual é a porcentagem do produto ? '))
pf = pi - (pi * pc /100)
print ('O produto que custava R${}, na promoção com desconto de {:.0f}% vai custar R${:.2f}'.format (pi,pc, pf))