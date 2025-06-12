carac = 0
def escreva (txt):
    carac = len(txt) + 4
    print('~' * carac)
    print(f'  {txt}')
    # print(carac)
    print('~' * carac)

# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('DEV')