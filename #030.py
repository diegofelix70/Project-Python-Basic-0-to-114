#Crie um programa que leia im número inteiro e mostre na tela se ele é par ou impar.

numero = int(input('Escolha um número e eu vou falar se ele é PAR ou IMPAR:  '))

#Se usa para a resolução: '%'  Resto da Divisão, sendo que se pode dar somente dois resultado, qualquer que for dividido vai 0 e o que não for (impar), vai dar 1.

resultado = numero % 2

if resultado == 0:
    print(f'O número {numero} é PAR.')
else:
    print(f'O número {numero} é ÍMPAR.')
