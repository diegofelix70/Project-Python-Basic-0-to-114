#Escreva um programa que leia um valor em metros e o exiba convertido em cintimetros e melimetros

n1 = int(input('Adicione um valor '))

cm = n1 * 100
mm = cm * 10

print('{0}mt em centimetros é: {1}cm e {0}mt em melimetros é: {2}mm.'.format(n1, cm, mm))