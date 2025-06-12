matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []
somap = somater = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}][{c}]:'))
        if matriz[l][c] % 2 == 0:
            somap += (matriz[l][c])
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {somap}')
for l in range(0, 3):
    somater += (matriz[l][2])
for c in range(0, 3):
    if c == 0:
        matriz[1][c] = mai
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]

print(f'A soma dos valores da terceira coluna é {somater}')
print(f'O maior valor da segunda linha é {mai}')





# A soma dos valores da terceira coluna
# O maior valor da segunda linha