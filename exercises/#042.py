'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 == n2 and n1 == n3 and n2 == n3:
    print('Equilátero')
elif n1 == n2 and n1 == n3 and n3 != n2:
    print('Isósceles')
elif n2 == n3:
    print('Isósceles')
else:
    print('Escaleno')'''

#EX Curso
#Primeiro ele captura a aula #35 para acrescentar essa aula.
v1 = int(input('Adicione o valor 1: '))
v2 = int(input('Adicione o valor 2: '))
v3 = int(input('Adicione o valor 3: '))

#EX CURSO
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v2 + v1: #Não tem diversar opções, ou é ou não é, por esse motivotem que se usar if dentro do if.
    if v1 == v2 == v3: #Diferente de outras linguagens, o python aceita essa construção.
        print('Equilátero')
    elif v1 != v2 != v3 != v1:
        print('Escaleno')
    else:
        print('Esósceles')
else:
    print('Não formam um triangulo.')