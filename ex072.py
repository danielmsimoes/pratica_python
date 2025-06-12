while True:
    num = int(input('Digite um número entre 0 e 20:'))
    if num > 20 or num < 0:
        print('Tente novamente')
    else:
        break
lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num1 = (lista[num])
print(f'Você digitou o número {num1}')
