jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('<->' * 20)
print(jogador)
print('<->' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('<->' * 20)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')