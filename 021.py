def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')



































# Interactive Help
# help(print)
# print(input.__doc__)

# docstrings = manual
# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela
#     :param i: O início da contagem
#     :param f: O fim da contagem
#     :param p: O passo da contagem
#     :return: sem retorno
#     Função feita por Daniel
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM!!')
#
#
# help(contador)
# contador(2, 10, 2)


# Argumentos opcionais
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma vale {s}')
#
#
# somar(3, 2, 5)
# somar(8, 4)

# Escopo de variáveis
# def teste(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
#
# a = 5
# teste(a)
# print(f'A fora vale {a}')
# print(f'B fora vale {b}')
# print(f'C fora vale {c}')


# def teste():
#     x = 8
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')
#
#
# # Programa principal
# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'No programa principal, x vale {x}')

# Retorno de resultados,
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(6)
#
# print(f'Os resultados foram {r1}, {r2} e {r3}')












