lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador',
         'futuro')

for item in lista:
    # print(item, end= ', ')
    print(f'\nNa palavra {item.upper()} temos ', end='')
    for letra in item:
        if letra in 'aeiou':
            print(letra, end=' ')