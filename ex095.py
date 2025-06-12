jogadores = {}
time = []  # tudo
partidas = []  # gols
while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do Jogador: ')).capitalize()
    partida = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    partidas.clear()
    for jogo in range(partida):
        partidas.append(int(input(f'Quantos gols na partida {jogo + 1} ?')))
        jogadores['gols'] = partidas[:]
        jogadores['total'] = sum(partidas)
    time.append(jogadores.copy())
    while True:
        continuar = str(input(f'Você quer continuar ? [S/N]')).capitalize()
        if continuar in 'SN':
            break
        print('ERRO! Respomda apenas S ou N.')
    if continuar == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
print('_' * 60)
for cod, v in enumerate(time):
    print(f'{cod} {v["nome"]:<15} {str(v["gols"]):<15} {v["total"]:<15}')
    print()
print('_' * 60)
while True:
    codigo = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if codigo == 999:
        break
    if codigo >= len(time):
        print(f'Erro! Não existe jogador com código {codigo}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[codigo]["nome"]}:')
        for i, v in enumerate(time[codigo]['gols']):
            print(f'    No jogo {i + 1} fez {v} gols')
print('<<< VOLTE SEMPRE >>>')





