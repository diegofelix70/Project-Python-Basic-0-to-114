print('='*30)
print('{:^30}'.format('Banco DFS'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cedula = 50 #Se começa com 50 porque é o máximo de celular que vamos dividir
tot__cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        tot__cedula += 1
    else:
        if tot__cedula > 0:
            print(f'Total de {tot__cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        tot__cedula = 0
        if total == 0:
            break
print('='*30)
print('Volte Sempre!')
