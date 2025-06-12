from datetime import date


def voto(a):
    print('_' * 35)
    ano1 = date.today().year
    idade = ano1 - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


ano = int(input('Em que ano você nasceu? '))
voto(ano)

