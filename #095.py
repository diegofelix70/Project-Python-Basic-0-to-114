time = list()
player = {}
gols = list()
while True:
    player.clear()

    player['name'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas pertidas {player["name"]} jogou? '))

    for c in range(0, tot):
        gols.append(int(input(f'Quantos gols você fez na partida {c}? ')))

    player['gols'] = gols[:] #Copiar a lista no dicionário porque a lista sempre começa zerada.
    player['total'] = sum(gols)

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda somente S ou N.')
    if resp == 'N':
        break
    
    time.append(player.copy())
print('-=-'*20)


print('Cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-=-'*20)

for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-=-'*20)


while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 para Finalizar programa)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(time) - 1:
        print(f'Notas de {time[opc][0]} são {time[opc][1]}')