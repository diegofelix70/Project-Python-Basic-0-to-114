v1 = int(input('Adicione o valor 1: '))
v2 = int(input('Adicione o valor 2: '))
v3 = int(input('Adicione o valor 3: '))

"""if v1 > v2 + v3:
    print('Não')
elif v2 > v1 + v3:
    print('não')
elif v3 > v2 + v1:
    print('não')
else:
    print('Sim')"""

#EX CURSO
if v1 > v2 + v3 and v2 > v1 + v3 and v3 > v2 + v1:
    print('Não')
else:
    print('Sim')