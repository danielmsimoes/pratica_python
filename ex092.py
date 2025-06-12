from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: ')).capitalize()
ano = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.now().year - ano
cadastro['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')