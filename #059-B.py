sair = False

while not sair:
    v1 = int(input('Primeiro valor: '))
    v2 = int(input('Segundo Valor: '))
    
    print('''
          [ 1 ] Somar
          [ 2 ] Multiplicar
          [ 3 ] Maior
          [ 4 ] Novos Número
          [ 4 ] Sair do programa''')
    jogador = int(input('>>> Qual a sua opção? '))
    
    if jogador == 1:
        soma = v1 + v2
        print(f'A soma entre eles é: {soma}.')
    elif jogador == 2:
        multi = v1 * v2
    elif jogador == 4:
        sair = True

print('Fim do Programa')