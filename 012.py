nome = str(input('Qual o seu nome?'))
n1 = nome.capitalize()
if n1 == 'Daniel':
    print('Que nome legal!')
elif n1 == 'João' or n1 == 'Thamires' or n1 == 'Rebecca':
    print ('Seu nome é muito bonito!')
elif n1 in 'Cleuza Jubscreudo Eldimilta':
    print ('Que nome esquisitokkkkf')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(n1))