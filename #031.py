#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e 0,45 para viagens mais longas.

quantidade = float(input('Quantos Km vão ser na sua viagem? '))

"""abaixo = quantidade * 0.50
abaixoFixo = 200 * 0.50

acima = (quantidade - 200) * 0.45
extra = abaixoFixo + acima

print('-=-'*20)

if quantidade >=200:
    print(f'O valor da passagem vai ser de {extra}. Pois você vai viajar {quantidade} de Km.')
else:
    print(f'O valor da passagem vai ser de {abaixo}. Pois você vai viajar {quantidade} de Km.')

print('Boa viajem! Obrigado por viajar com nós.')
print('-=-'*20)"""

#EX Curso

"""if quantidade <= 200:
    preco = quantidade * 0.5 #Aqui pode fazer direto de dentro da função.
else:
    preco = quantidade *0.45 #Aqui eu posso repetir porque o programa vai mostrar somente o verdadeiro."""

preco = quantidade * 0.50 if quantidade <= 200 else quantidade *0.45 # aqui eu posso fazer na mesma linha.

print(f'E o preço da sua passagem será de R${preco:.2f}')