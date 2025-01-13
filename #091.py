from random import randint
from operator import itemgetter
from time import sleep
player = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
ranking = () #Para ser ordenado se recomenda smepre jogar em uma lista
print('-=-=-= Valores Sorteados =-=-=-')
for k, v in player.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(player.items(), key=itemgetter(1), reverse=True)

print('-=-'*30)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)