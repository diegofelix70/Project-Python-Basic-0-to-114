num = int(input('Adicione um número: '))
c = num
f=1
print(f'Calculando o fatorial de {num}!: ',end='')
while  c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f'{f}')