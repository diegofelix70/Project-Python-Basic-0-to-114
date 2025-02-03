#Escreva um programa que leia a verlocidade de um carro.
 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

#A multa vai custar R$7,00 por cada Km acima do limite.

from random import randint
velocidade = randint(60, 100)

multa = (velocidade - 80) *7
print('-=-'*20)
print('>>> NOTIFICAÇÃO DA NOVA DUTRA <<<')

if velocidade <= 80:
    print(f'Tudo certo! Sua velocidade era de {velocidade}Km/h, por isso você não foi multado.')
else:
    print(f'Você foi multado em R${multa:.2f}, pois a sua velocidade estava a {velocidade}Km/h.')
    
print('Obrigado por viajar nas estradas da Nova Dutra!')
print('-=-'*20)
