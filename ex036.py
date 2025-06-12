casa = float(input ('Qual será o valor da casa ?'))
salário = float(input ('Qual é o seu salário ?'))
anos = int (input ('Em quantos anos a casa será paga ?'))
mes = anos * 12
porcentagem = (salário * 30) / 100
prestacao = casa / mes
if prestacao > porcentagem:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
    print ('O empréstimo foi negado')
elif prestacao <= porcentagem:
    print('Para pagar uma casa de {:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
    print ('Seu empréstimo foi aceito')