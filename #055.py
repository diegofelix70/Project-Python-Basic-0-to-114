#Crie um programa que leia o peso de cinco pessoas. No final mostre qual doi o meior e o menor peso lidos.


'''p = 1
peso__maior = 0
peso__menor = 0

for c in range(1, 6):
    peso = int(input(f'Peso da {p}ª pessoa? '))
    p = p + 1
    peso__menor = peso
    

    if peso > peso__maior:
        peso__maior = peso
        print(f'o numero  {peso__maior}')
    elif peso < peso__menor:
        peso__menor = peso
        print(f'o numero  {peso__menor}')
    else:
        peso__menor = peso
print(peso__maior)
print(peso__menor)
'''


# Referencias #
'''Atividade #054'''

#EX Curso

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}')
print(f'O menor peso foi {menor}')