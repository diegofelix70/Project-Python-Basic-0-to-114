#Crie um programa que vai gerar cinco números aleatórios e colocar em uma Tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e maior valor que estão na Tupla

from random import randint

aleatorio = randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5)

print('Os números sorteados foram: ', end='')
for n in aleatorio:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(aleatorio)}')#Esse max pega somente dentro de uma lista, ela não faz lista automatica em um while ou if.
print(f'O maior valor sorteado foi: {min(aleatorio)}')