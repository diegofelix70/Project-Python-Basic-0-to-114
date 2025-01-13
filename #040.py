#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
n4 = float(input('Nota 4: '))

m = (n1 + n2 + n3 + n4) / 4

print('Sua nota foi {}.' .format(m))
if m > 7:
    print('Aprovado')
elif m < 5:
    print('Reprovado')
else:
    print('Em Recuperação')