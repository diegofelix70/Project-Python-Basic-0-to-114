#Escreva um programa qie leia dois números inteiros e compare-os, mostrando na tema uma mensagem:

"""data = float(input('Ano de nascimento: '))
age = 2024 - data
still = 18 - age

if age < 18:
    print('Ainda vai se alistar.')
    print('Falta {:.0f} anos para você se alistar'.format(still))
elif age == 18:
    print('Hora de se alistar.')
else:
    print('Passou da hora de se alistar.')"""

#EX Curso

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

if idade == 18:
    print('Hora de se alistar.')
elif idade < 18:
    still = 18 - idade
    print('Ainda vai se alistar.')
    print('Falta {:.0f} anos para você se alistar'.format(still))
elif idade > 18:
    print('Passou da hora de se alistar.')