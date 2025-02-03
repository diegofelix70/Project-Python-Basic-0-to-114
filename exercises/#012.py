# Faça um algoritmo que leia o preço de um profuto e mostre o seu novo preço, com 5% de desconto.

'''produto = int(input('Preço do produto? '))

valorfinal = (produto/100) *95

print(f'O valor com 5% de deconto é: {valorfinal:.0f}')'''



produto = int(input('valor do produto: '))
porcentagemreceber = int(input('quanto vai ser a porcentagem? '))

valorfinal = produto - (produto * porcentagemreceber / 100)

print(f'o valor final fica: {valorfinal:.0f}')