#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

#O programa deverá escrever na tela se o uruário venceu ou perdeu.

"""import random
num = int(input('''Digite um número inteiro na tela de 0 a 5 e tente adivinhar o número que o computador escolheu.
Qual o seu palpite de sorte: '''))

lista = [0, 1, 2, 3, 4, 5] # Aqui eu fiz uma lista da quantidade de números que eu quero que o computador gere aleatoriamente.
aleatorio = random.choice(lista)

if num == aleatorio:
    print('Belo chute! Você acertou.')
else:
    print('Não foi dessa vez! Mais sorte na próxima vez.')
print(f'O número que o computador escolheu aleatoriamente foi: {aleatorio}!')"""

#Seguindo o Curso:

from random import randint #Ao inves do "choice", onde ue tenha que criar a lista, aqui ele escolheu dentro da biblioteca o "randint", que gera o número que eu pedir dentro de parentes usando a virgula.
from time import sleep #Essa função da um time para aparecer ativar a próxima função

computador = randint(0, 5)
print('-=-'*20) #Sempre que eu fazer alguma solução depois das aspas simples ele vai seguir no print. No caso  aqui ele vai multiplicar em 20x
print('Vou pensar em número de 0 a 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei: '))
print('PROCESSANDO...')

sleep(1) # Entre parenteses eu coloco o tempo que vai ficar off até chamar a próxima função.

if jogador == computador:
    print('Parabéns! Você consguiu me vender!')
else:
    print(f'Não foi dessa vez! O número que o computador escolheu foi: {computador}!')