# Função perfsonalizada
# def
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)







# empacotar
# def contador(*num):
#     tamanho = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tamanho} números')
#
#
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)


# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
#     print()
#
#
# numero1 = int(input('Numero1: '))
# numero2 = int(input('Numero2: '))
# soma(numero1, numero2)
# soma(4, 4)
# soma(a=1, b=7)






















# def titulo(txt):
#     print('-'*30)
#     print(txt)
#     print('-'*30)
#
#
# titulo('    Daniel Simões    ')
# titulo('    Curso em vídeo    ')
# titulo('    Aprenda python    ')











# def linha():
#     print('=-' * 30)
#
#
# linha()
# print('    Curso em vídeo    ')
# print('    Aprenda python    ')
# print('    Daniel Simões    ')
# linha()
