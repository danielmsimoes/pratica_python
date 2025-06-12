cores = {'limpa': '\033[m',
         'vermelho': '\033[31m'}


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('{}ERRO! Digite um número inteiro válido.{}'.format(cores['vermelho'], cores['limpa']))
            continue
        except (KeyboardInterrupt):
            print('{}ERRO! Usuário preferiu não digitar esse número {}'.format(cores['vermelho'], cores['limpa']))
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print('{}ERRO! Digite um número real válido.{}'.format(cores['vermelho'], cores['limpa']))
            continue
        except (KeyboardInterrupt):
            print('{}ERRO! Usuário preferiu não digitar esse número {}'.format(cores['vermelho'], cores['limpa']))
        else:
            return r


# Programa Principal
n = leiaInt('Digite um Inteiro: ')
r = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r}')
