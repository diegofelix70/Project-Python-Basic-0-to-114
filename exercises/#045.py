#Crie um programa que faça o computador jogar jokempô com você.

'''import random

print('='*20)
print('Vamos jogar JOKEMPÔ?
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura')

escolha = int(input('Escolha um número: '))

nome = [1,2,3]
escolhido = random.choice(nome)'''

#EX Curso

from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) #Se conta a partir do 0 = 1

print('''Suas opçãoes
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual vai ser a sua jogada? '))

print('Jo...')
sleep(1)
print('Ken...')
sleep(1)
print('Pôô')

print('-=-'*9)
print(f'o computador escolheu {itens[computador]}') #Depois de ter feito uma lista, adicionando o nome da vareavel random entre chaves, aparece o nome.
print(f'O jogador escolheu: {itens[jogador]}.')
print('-=-'*10)

if computador == 0:#Computador escolheu PEDRA. #Aqui vamos partir do momento onde o computador vai escolher uma opção antes do jogador.
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador ==2:
        print('Computador VENCEU')

elif computador == 1: #Computador escolheu PAPEL.
    if jogador == 0:
        print('Computador VENCEU')
    elif jogador == 1:
        print('Empate')
    elif jogador ==2:
        print('Jogador VENCEU')

elif computador == 2: #Computador escolheu TESOURA.
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador ==2:
        print('Empate')
