#\033[style;text;back m
# style = 0;1;4;7
# text = 30 - 37
# back 40 - 47
'''print ('\033[7;30;45mOlá Mundo\033[m')'''
'''a = 5
b = 8
print ('OS valores são \033[35m{}\033[m e \033[4;30;47m{}\033[m'.format(a, b))'''
# para facilitar usando variáveis
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'vermelho':'\033[31m'}
nome = 'Daniel'
print ('Olá muito prazer em te conhecer, {}{}{}'.format(cores['vermelho'], nome, cores['limpa']))

