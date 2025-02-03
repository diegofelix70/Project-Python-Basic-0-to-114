# Crie um algoritmo que çeia um número e mostre o seu dobro tripo e raiz quadrado.
#PAra fazer Raiz Quadrada além de usar "n1 ** (1/2)" eu tambpém posso usar "pow(n, (1/2))".

n1 = int(input('Adiociona um valor '))

d = n1 * 2
t = n1 * 3
q = n1 ** (1/2)

print('Dobro {}. \n Triplo {}. \n Raiz Quadra{}.'.format(d, t, q))