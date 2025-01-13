#Primeiro valor:
# Segundo valor:
#   [1] Somar.
#   [2]Multiplicar.
#   [3]Maior.
#   [4] Novos números.
#   [5]Sair do programa
# >>>>> Qual é a sua opção?.

'''Primeiro = int(input('Primeiro valor: '))
Segundo = int(input('Segundo valor: '))

soma = Primeiro + Segundo
mult = Primeiro * Segundo

print(' [1] Somar. \n [2] Multiplicar.   \n [3] Maior.   \n [4] Novos números.   \n [5] Sair do programa')

escolha = int(input('>>>>> Qual é a sua opção? '))

while escolha != 5:
    if escolha == 1:
        print(f'Soma é {soma}')
    elif escolha == 2:
        print(f'A multiplicação é {mult}')
    elif escolha == 3:
        if Primeiro > Segundo:
            print(f'O {Primeiro} é maior')
    else print(f'O {Segundo} é maior')
print('fim')
    '''

'''n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print(   [1] Somar
    [2] Multiplicar 
    [3] Maior
    [4] Novos números
    [5] Sair do programa)
    opção = int(input('Qual é a sua opção? '))
print('Fim do programa')'''

'''n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print(    [1] Somar
    [2] Multiplicar 
    [3] Maior
    [4] Novos números
    [5] Sair do programa)
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:

    elif opção == 2:

    elif opção == 3:

    elif opção == 4:

    elif opção == 5:

    else:
        print('Opção inválida. Tente Novamente')
    print('=-=' * 10)

print('Fim do programa')'''

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar 
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {mult}')
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif opção == 4:
        print('Informe novamente ')
        n1 = int(input('Primeiro número '))
        n1 = int(input('Segundo número '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente Novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa')