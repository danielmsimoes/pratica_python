n = int (input('Digite um número inteiro:'))
print(f'''
[1] converter {n} para BINÁRIO
[2] converter {n} para OCTAL
[3] converter {n} para HEXADECIMAL''')
opcao = (input('Sua opção: '))
if opcao == '1':

    n1 = bin(n)
    n2 = n1[2:]
    n3 = opcao = 'BINÁRIO'
if opcao == '2':
    n1 = oct(n)
    n2 = n1[2:]
    n3 = opcao = 'OCTAL'

if opcao == '3':
    n1 = hex(n)
    n2 = n1[2:]
    n3 = opcao = 'HEXADECIMAL'
print (f'{n} convertido para {n3} é igual a {n2} ')
