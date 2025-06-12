lista = []
while True:
    valor = int(input('Digite um valor:'))
    if valor in lista:
        print('Valor duplicado! Não será adicionado...')
    else:
        print('Valor adicionado com sucesso...')
        lista.append(valor)
    resposta = input('Quer continuar ? [S/N]').capitalize()
    if resposta == 'N':
        break
lista.sort()
print('-='*30)
print(f'Você digitou os valores {lista}')

