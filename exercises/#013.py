# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

Salário = int(input('Valor do salário: '))

final = Salário + (Salário * 15 / 100)

print(f'Seu salário com 15% de aumento fica: {final:.0f}')