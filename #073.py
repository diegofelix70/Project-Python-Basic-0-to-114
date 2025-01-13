#Crie uma tupla preenchida com os 20 primeiros colocados da Tebela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#Apenas os 5 primeiros colocados
#Os últimos 4 colocados
#Uma lista com os times em ordem alfabética.
#Em que posição na tabela está o seu time.

tabela__brasileirao = 'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Red Bull Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá'
print('-'*40)
print(tabela__brasileirao[:5])
print('-'*40)
print(tabela__brasileirao[-4:])
print('-'*40)
print(sorted(tabela__brasileirao))
print('-'*40)
#print(tabela__brasileirao[5])
#EX CURSO
position = input('De qual time você quer ver a posição? ')
print(f'O São Paulo está na {tabela__brasileirao.index(position)}º posição do Brasileirão')
print('-'*40)
