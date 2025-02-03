#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n1 = int(input('Adione um número '))
a = n1 * 2
b = n1 * 3
c = n1 * 4
d = n1 * 5
e = n1 * 6
f = n1 * 7
g = n1 * 8
h = n1 * 9
i = n1 * 10

print('A taboada desse número é: \n {0}x1{0} \n {0}x2{1} \n {0}x3{2} \n {0}x4{3} \n {0}x5{4} \n {0}x6{5} \n {0}x7{6} \n {0}x8{7} \n {0}x9{8} \n {0}x10{9}'.format(n1, a, b, c, d, e, f, g, h, i))

#Resolução:
#Por ser um número quebrado, começar com "float"

n1 = float(input('Primeira'))
n2 = float(input('Segunda'))

m = (n1 + n2) /2 

print('A média entre {} e {} é igual a {:.1f}.'.format(n1, n2, m))