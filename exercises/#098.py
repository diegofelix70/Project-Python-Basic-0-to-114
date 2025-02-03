from time import sleep

def estilo():
    print('-=-' * 20)

'''print('Contagem de 1 até 10 de 1 em 1')'''
#Não se usa o for se não tem pré-estabelecido o que usar
'''for c in range(11, 0):
    print(f'{c} ')
    c += 1
    sleep(1)'''

# EX Curso
def contador(i, f, p):
    estilo()

    #Coloca esse teste antes para não acusar no print da mensagem
    if p < 0: # Isso para parar no zero e não contar negativo
        p *= -1

    if p == 0: # Para não parar no zero
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)


    if i < f: # Para contar de ordem crescente
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True) # Se usa o flosh=True para quebrar o buffer de tela, assim não ele não precisa de concluir a lógica para mostrar na tela.
            sleep(0.5)
            cont += p # Contador crescente
        print('FIM!')

    else:
        cont = i
        while cont >= f: # Para contar na ordem decrescente
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p # Contador Decrescente
        print('FIM!')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)

# Fim do programa com definições pré-estabelecida
estilo()
print('Agora é a sua vez de personalizar a contagem')
ini = int(input('Início: '))
fim = int(input('fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)