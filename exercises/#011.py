# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, printa uma área de 2m2. 

l = float(input('Coloque o valor da altura '))
a = float(input('Coloque o valor da largura '))

area = (l * a) /2

print('O valor de tinta necessário para pintar é {:.1f} litros.'.format(area))