def dobro(preço=0, f=False):
    res = preço * 2
    return res if f is False else moeda(res)


def metade(preço=0, f=False):
    res = preço / 2
    return res if f is False else moeda(res)


def aumentar(preço=0, taxa=0, f=False):
    res = preço + (preço * taxa/100)
    return res if f is False else moeda(res)


def diminuir(preço=0, taxa=0, f=False):
    res = preço - (preço * taxa/100)
    return res if f is False else moeda(res)


def moeda(preço=0, moeda='R$', f=False):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(n, taxaa=0, taxad=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(n, taxaa, True)}')
    print(f'{taxad}% de redução: \t{diminuir(n, taxad, True)}')
