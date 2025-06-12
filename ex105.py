def notas(*n, sit=False):
    '''
    -> Recebe as notas de alunos e faz uma análise
    :param n: Notas podem ser mais de uma
    :param sit: (OPCIONAL) traz a situação da média
    :return: mostra o total de notas, a maior, a menor e a média.
    '''
    t = dict()
    t['total'] = len(n)
    t['maior'] = max(n)
    t['menor'] = min(n)
    t['media'] = sum(n) / len(n)
    if sit:
        if t['media'] >= 9:
            t['situação'] = 'EXCELENTE'
        elif t['media'] >= 7:
            t['situação'] = 'BOA'
        elif t['media'] >= 5:
            t['situação'] = 'RAZOÁVEL'
        else:
            t['situação'] = 'RUIM'
    return t


# Programa Principal
resp = notas(9.5, 9.5, 10, 8.5, sit=True)
print(resp)
