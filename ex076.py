count = 0
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Tranferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livros', 34.90)
for item in range(len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}' , end='')
    else:
        print(f'R${lista[item]:>7.2f}')
print('-'*40)