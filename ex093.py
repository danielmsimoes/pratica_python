jogador = dict()
soma = 0
lista = []
jogador['nome'] = str(input('Nome do jogador:')).capitalize()
c = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
for v in range(c):
    gol = int(input(f'Quantos gols na partida {v}?'))
    lista.append(gol)
    jogador['gols'] = lista
jogador['total'] = sum(lista)
print('=-' * 30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {c} partidas.')
for v in range(c):
    print(f'=> Na partida {v}, fez {lista[v]} gols.')
print(f'=> Foi um total de {jogador["total"]} ')