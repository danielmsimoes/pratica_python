da = int(input ('Quantos dias alugados ?'))
kmr = float (input('Quantos km rodados ?'))
daf = 60 * da
kmrf = 0.15 * kmr
vt = daf + kmrf
print ('O total a pagar é de R${:.2f}'.format (vt))