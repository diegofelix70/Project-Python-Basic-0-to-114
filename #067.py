cont = taboada = 0
while True:
    numero = int(input('Quer ver a tubuada de qual valor? '))
    # if numero == -1: --> Qual foi Diego, é só colocar menor que 0 e tudo é negativo kkk
    if numero < 0:
        break

    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')
    print('='*10)
print('Fim')