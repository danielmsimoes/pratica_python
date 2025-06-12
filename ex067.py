num = 0
while True:
    print('-' * 20)
    num = int(input('Quer ver a tabuada de qual valor ?'))
    print('-' * 20)
    if num < 0:
        break
    for t in range(1, 11):
        m = t * num
        print(f'{num} x {t} = {m}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
