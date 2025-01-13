#Faça um mini-sistema que utilize o interactive gilp do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra fum, o programa se encerrará.

# Base do programa

'''def ajuda(com):
    help(com)

# Comamando principal
comando = ''
while True:
    comando =str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)'''
c = ('\033[m',        # 0 - Quebrar sequencia de cores
       '\033[0;30;41m', # 1 - Vermelho
       '\033[0;30;42m', # 2 - Verde
       '\033[0;30;43m', # 3 - Amarelo
       '\033[0;30;44m', # 4 - Azul
       '\033[0;30;45m'  # 5 - Roxo
       '\033[7;30m'     # 6 - Branco
       )

def ajuda(com): # Chamar o HELP
    help(com)

def titulo(msg, cor=0): # Estilo dos titulos
    tam = len(msg) + 4 # Colocando espaçamento das laterais
    print(c[cor], end='') # Inicio da cor de fundo
    print('~' *tam)
    print(f'  {msg}') #dois espaços no começo para centralizar
    print('~' * tam)
    print(c[0], end='') # Fim da cor de fundo

# Comamando principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2) # Esse 2 é a cor
    comando =str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)