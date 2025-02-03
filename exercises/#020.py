#Para criar uma lista e sortear ela fazendo uma lista, exemplo: ordem de apresentação, se usa: "shuffle".

import random

p = str(input('Primeiro nome: '))
s = str(input('Segundo nome: '))
t = str(input('Terceiro nome: '))
q = str(input('Quarto nome: '))

lista = [p, s, t, q]

random.shuffle(lista) #

mensagem = f'a ordem de apresentação será: {lista}.'

print(mensagem)