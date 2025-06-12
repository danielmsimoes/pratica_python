a = float(input ('Qual é a altura da sua parede em metros ? '))
l = float(input ('Qual é a largura da sua parede ? '))
at = a * l
atf = at / 2
print ('Sua parede tem a dimensão de {}x{}, e sua área é de {} m².'.format (a, l, at),end='')
print ('Para pintar essa parede, você presisará de {}l de tinta.'.format (atf))