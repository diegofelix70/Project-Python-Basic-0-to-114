tot__price = menor__price = mil__price = tot__mil = cont = 0
nome__produto = ' '

while True:
    continuar = ' '

    produto = str(input('Nome do Produto: '))

    price = int(input('Preço do produto: R$'))
    tot__price += price
    cont += 1

    if cont == 1:
    #if price == 1: # PAra essa lógica dar certo, você precisa de um contador para contar os números. EX: quanto o contador pegar o primeiro produto '== 1' ele vai fazer a lógica para colocar o valor na variavel de menor preço.
        menor__price = price
        nome__produto = produto

    else: 
        if price < menor__price:
            menor__price = price
            nome__produto = produto

    if price > 1000:
        mil__price = price
        tot__mil += 1


    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('\nFim do Programa')
print(f'O total de compra foi {tot__price}')
print(f'Temos {tot__mil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {nome__produto} e custou {menor__price}')