from datetime import date
ano = int(input('Ano de nascimento:'))
atual = date.today().year
ano1 = atual - ano
print(f'Quem nasceu em {ano} tem {ano1} em {atual}')
if ano1 < 18:
    a = ano1 - 18
    print(f'Ainda faltam {a} anos para o alistamento.')

elif ano1 > 18:
    a = ano1 - 18
    b = 2023 - a
    print(f'Você já deveria ter se alistado há {a} anos.')
    print(f'Seu alistamento foi em {b}')

elif ano1 == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
