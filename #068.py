#Faça um programa que johue par ou impar com o computador. O jogo só será imterrompido quando o kogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''from random import randint

escolha = ''
vencedor = ''
while True:
    
    computador = randint(0, 10)

    print('='*40)
    print('Vamos jogar PAR ou ÍMPAR = Quero ver você me vencer!!!')
    print('='*40)
    numero = int(input('Diga um valor: '))
    escolha__pessoa = int(input('Par ou Ímpar [P/I]? '))
    resultado = numero + computador

    resultado__teste = numero % computador
    if resultado__teste == 0:
        escolha = 'Par'
    else:
        escolha = 'Ímpar'
    
    if escolha__pessoa == 'I':


    print('-'*40)
    print(f'Você escolheu {numero} e o computador escolheu {computador}. O total de {resultado} deu {escolha}.')'''


from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper() [0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEI ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAMER OVER! Você venceu {v} vezes.')