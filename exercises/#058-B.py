#Melhore o jogo DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adbinhar até acertar, mostyrando no final quantos papelites foram necessários para vender.

'''from random import randint 
from time import sleep 

cont = 0

print('-=-'*20)
print('Vou pensar em número de 0 a 5. Tente adivinhar...')
print('-=-'*20)

computador = randint(0, 5)

while computador != jogador:
    jogador = int(input('Tente novamente: '))
    if jogador == computador:
        cont + 1
print('Acertou!')'''

from random import randint 

computador = randint(0, 10)

print('Vou pensar em número de 0 a 10. Tente adivinhar...')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente novamente: ')
        elif jogador < computador:
            print('MAis... Tente novamente: ')
print(f'Acertou com {palpites} tentativas. Parabéns')