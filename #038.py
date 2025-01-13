#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

PN = float(input('Primeiro número: '))
SN = float(input('Segundo número: '))

if PN > SN:
    print('Valor.')
elif PN < SN:
    print('Valor menor')
else:
    print('Numeros iguais.')