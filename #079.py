# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o númeor já exista lá dentro, ele não será adicionado. No final, serão ecibidos todos os valores úinicos digitados, em ordem cresacente.
'''lista = []'''
number = list()

while True:
    continuar = ' '
    '''lista.append(int(input('Digite um valor: ')))'''
    n = int(input('Digite um valor: '))

    if n not in number:
        number.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor Duplicado! Não vou adicionar na lista...')

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=-'*25)
number.sort()
print(f'Você digitou os valores: {number}')
