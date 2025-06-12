ca = float(input ('Quanto dinheiro você tem na carteira R$ :'))
d = 5.26
e = 6.02
li = 7.12
ien = 0.046
vfe = ca / e
vfd  = ca / d
vfli = ca / li
vfien = ca / ien

print ('Com R${:.2f} \n Você consegue comprar \n US${:.2f} \n €{:.2f} \n £{:.2f} \n ¥{:.2f} '.format (ca, vfd, vfe, vfli, vfien))