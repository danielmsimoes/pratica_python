def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO! Usuário preferiu não digitar esse número {}\033[m')
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu (lista):
    cabecalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[034m{item}\033[m')
        cont +=1
    print(linha())
    opc = leiaInt('\033[32mSua Opção:\033[m')
    return opc