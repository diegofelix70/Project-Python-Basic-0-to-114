'''Faça um programa que calcule a soma de todos os numeros impares que são multiplos de tres que se encontram no intervalo de 1 até 500.'''

#Aqui mostra somente os números que fazem divisão de 3
'''for i in range(0, 500+1):
    if i / 3 == 0:
        print(i, end=' ')'''

#Aqui mostra a soma desses números que se fazem divisão de 3
'''soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
print('A soma é: {}.'.format(soma))'''

#Aqui vai contar quantas vezes aparece um número que faz divisão de 3 e vai mostrar o resultados desses números
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i #quando é a própria "intereção", ele geralmente somente acomula 
        cont = cont + 1 #quanto eu colo o sinal "número", ele conta ele mais ele mesmo.
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))