def factorial(n, conta):
    print('-' * 30)
    """
    -> Calcula o Fatorial de um número
    :param n: O número a ser calculado
    :param conta: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número (n)
    """
    from math import factorial
    resp = factorial(n)
    if conta:
        for c in range(n, 1, -1):
            print(f'{c} x ', end='')
            if c == 2:
                print('1', end='')
        print(f' = {resp}')
    else:
        print(f'{resp}')


factorial(5, True)
# help(factorial)