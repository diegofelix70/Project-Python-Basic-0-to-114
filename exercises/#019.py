#Parênteses (): Usados para chamar funções e métodos, e para agrupar expressões.
#Colchetes []: Usados para definir listas, acessar elementos de listas e dicionários, e em expressões de compreensão de listas.

#O método random.randint() é usado para gerar um número inteiro aleatório dentro de um intervalo específico, e não para selecionar um item de uma lista.

#Para escolher aleatoriamente entre os nomes informados, você deve colocar os nomes em uma lista e usar a função random.choice().

import random
a = input('infomrme um nome: ') #Se não for capturar somente número não precisa de str, int, float... Pode começar direto com input
b = input('infomrme um nome: ')
c = input('infomrme um nome: ')
d = input('infomrme um nome: ')
nome = [a,b,c,d]
escolhido = random.choice(nome)
print('O nome escolhido foi {}.'.format(escolhido))