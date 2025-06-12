lista = []
v = str(input('Digite a expressão: '))
for simb in v:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão matemática está válida!')
else:
    print('Sua expressão matemática está inválida!')






# v = str (input('Digite a expressão: '))
# lista = [v]
# aberto = v.count('(')
# fechado = v.count(')')
# if aberto == fechado:
#     print('Sua expressão matemática está válida!')
# else:
#     print('Sua expressão matemática está inválida!')


# ((a+b)*c)(x+y(3+2/3)*z)