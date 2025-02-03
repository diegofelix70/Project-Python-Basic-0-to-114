number = list()
par = list()
impar = list()

cont = 0
while True:
    continuar = ' '

    n = (int(input('Digite um valor: ')))

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    
    number.append(n)


    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=-'*25)
print(f'A lista completa é: {number}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')

