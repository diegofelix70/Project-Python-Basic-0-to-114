number = list()
cont = 0
while True:
    continuar = ' '
    number.append(int(input('Digite um valor: ')))
    cont +=1



    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=-'*25)
print(f'Você digitou {cont} elementos')
number.sort(reverse=True)
print(f'Os valores decrescentes são: {number}')
if 5 in number:
    print('O valor 5 está na lista.')
else:
    print('Valor não encontrado na lista.')
