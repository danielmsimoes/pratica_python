from time import sleep

def maior (* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando o valores passados...')
    sleep(0.5)
    tamanho = len(num)
    for valor in num:
        print(f'{valor}', end=' ')
        cont += 1
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
    print(f'Foram informados {tamanho} valores ao todo')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()