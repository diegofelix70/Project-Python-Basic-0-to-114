#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

#

import math
num = float(input('please, give me a number: '))
print('Your intire number is {}.'.format(math.trunc(num)))

from math import trunc
num = float(input('number: '))
print('number is {}.'.format(trunc(num)))

'''num = float(input('number: '))
print('number is {}{}{}.'.format(int('\033[0;34;40', num, '\033[40m')))'''