n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é \033[7;33;40m{}\033[m'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1])) # Se usa o -1 para contar de trás pra frente