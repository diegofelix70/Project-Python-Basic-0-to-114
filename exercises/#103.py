#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome,gols=0):
    if nome == '':
        nome = str('<desconhecido>')
    print(f'O jofador {nome} fez {gols} gols(s) no campeonato.')

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols')) 
# Verifica se o usuário não digitou nada em 'gols' e assume o valor 0
if gols.strip() == '': # Antes de deixar em 0 eu tenho que identificar se tem alguma coisa dentro.
    gols = 0
else:
    gols = int(gols) # Eu deixo como string para se caso não tiver nada, ele se transforme em um numero inteiro.
ficha(nome, gols)