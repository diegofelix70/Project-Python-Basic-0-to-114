#Elabore um produto que calcule o valor a ser pago por um produto, considerendo o seu preço normal e condição de pagamento:
#À vista dinheiro: 10%.
#À vista no cartão: 5%.
#Em até 2x o preço normal
#3x ou mais 20%.

print('-=-'*20)

preco = float(input('Informe o valor do produto: R$'))

print('''Infome como você vai pagar essa compra:
\033[1;30;44m[ 1 ]\033[m - Dinheiro;
\033[1;30;44m[ 2 ]\033[m - Cartão à vista;
\033[1;30;44m[ 3 ]\033[m - 2x sem juros;
\033[1;30;44m[ 4 ]\033[m - 3x com 20% de juros.''')
condicao = int(input('Digite o numero correspondente: '))

'''descdin = preco - (preco * 10 / 100)
desccart = preco - (preco * 5 / 100)
cart2x = preco
cart3x = preco + (preco * 20 / 100)

if condicao == 1:
    print(descdin)
elif condicao == 2:
    print(desccart)
elif condicao == 3:
    print(cart2x)
elif condicao == 4:
    print(cart3x)
else:
    print('Escolha somente de 1 a 4. Tente novamente!')'''

#EX Curso

if condicao == 1:
    total = preco - (preco * 10 / 100)
    print(total)
elif condicao == 2:
    total = preco - (preco * 5 / 100) #Dentro de cada um eu posso repetir o mesmo nome condição de antes, pois ela vai rodar somente dentro desse elif.
    print(total)
elif condicao == 3:
    total = preco
    print(total)
elif condicao == 4:
    total = preco + (preco * 20 / 100) 
    totparc = int(input('Em quantas vezes você vai parceçar? '))
    parcela = total / totparc
    print(f'Sua compra se´ra parcelado em {totparc} de {parcela}.')
else:
    print('Escolha somente de 1 a 4. Tente novamente!')
print(f'Sua compra vai dar R$ {total} no total.')

print('-=-'*20)
