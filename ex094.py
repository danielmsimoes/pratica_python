dados = {}
lista = []

media = soma = 0
while True:
    dados['nome'] = str(input('Nome:')).capitalize()
    dados['sexo'] = str(input('Sexo: [M/F]')).capitalize()
    while dados['sexo'] != 'M' and dados['sexo'] != 'F':
        print('ERRO! Por favor, digite apenas M ou F')
        dados['sexo'] = str(input('Sexo: [M/F]')).capitalize()
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    fim = str(input('Quer continuar ? [S/N]')).capitalize()
    if fim == 'N':
        break
    while fim != 'S' and 'N':
        print('ERRO! Por favor, digite apenas S ou N')
        fim = str(input('Quer continuar ? [S/N]')).capitalize()
media = (soma) / len(lista)
print('-=-' * 30)
print(f'A)  Ao todo temos {len(lista)} pessoas cadastradas')
print(f'B)  A média de idade é de {media:5.2f} anos.')
print(f'C)  As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print(f'D)  Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('     ', end='')
        for i, v in p.items():
            print(f'{i} = {v}; ', end='')
        print()
print('<<<  ENCERRADO  >>>')
