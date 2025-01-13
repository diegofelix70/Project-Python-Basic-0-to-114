#crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
#Conciderar a maior idade com 21 anos.

from datetime import date

tot__menos = 0
tot__mais = 0
p = 1

for c in range(1, 8):
    ano = int(input(f'Em que ano nasceu a {p}ª pessoa? '))
    p = p + 1
    idade = date.today().year - ano
    
    if idade > 21:
        tot__mais += 1
    else:
        tot__menos += 1

print(f'o numero de pessoas acima de 21 foram {tot__mais}')
print(f'o numero de pessoas abaixo de 21 foram {tot__menos}')


# Referencias pessoais #
'''from datetime import date

ano = int(input('Qual seu ano de nascimento: '))

idade = date.today().year - ano'''

'''soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i #quando é a própria "intereção", ele geralmente somente acomula 
        cont = cont + 1 #quanto eu colo o sinal "número", ele conta ele mais ele mesmo.
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))'''

'''soma = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
print(soma)'''