'''player = {}
gols = list()
player['name'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas pertidas {player["name"]} jogou? '))
for c in range(0, tot):
    gols.append(int(input(f'Quantos gols você fez na partida {c}? ')))


print(player) 
print(gols) '''

player = {}
gols = list()
player['name'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas pertidas {player["name"]} jogou? '))

for c in range(0, tot):
    gols.append(int(input(f'Quantos gols você fez na partida {c}? ')))

player['gols'] = gols[:] #Copiar a lista no dicionário porque a lista sempre começa zerada.
player['total'] = sum(gols)

print('-=-'*30)

print(player)

print('-=-'*30)

for k, v in enumerate(player.items()):
    print(f'O campo {k} tem o valor de {v}.')

print('-=-'*30)

print(f'O jogador {player["name"]} jogou {len(player["gols"])} partidas.')
for i, v in enumerate(player['gols']):
    print(f'=> Na partida {i}, vez {v} gols.')
print(f'Foi um total de {player["total"]} gols.')