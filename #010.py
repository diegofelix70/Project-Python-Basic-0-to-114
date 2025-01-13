# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comrpar = Considere US$1,00 == R$3,27

n1 = int(input('Valor em real? R$'))
r = n1 / 6.01 #dolar no dia 12/12/24
print(f'Com R${n1} você pode comprar ${r:.2f}.')