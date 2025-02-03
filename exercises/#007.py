#Desvenvolva um programa que leia as duas notas de uma anulo e calcule e sua média.

n1 = int(input('Adicione uma nota'))
n2 = int(input('Adicione uma nota'))
n3 = int(input('Adicione uma nota'))
n4 = int(input('Adicione uma nota'))

s = n1 + n2 + n3 + n4
m = s / 4

print('Sua média é: {}'.format(m))

# Colocar "float"