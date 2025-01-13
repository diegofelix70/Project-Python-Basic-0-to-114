#Desenvolva um programa que leia quantro valores pelo texlado e guarde-os em uma tupla. No final, mostre:
#A = Quantas vezes apareceu o valor "9"
#Em que posição foi digitado o primeiro "3"
#Quais foram os números pares.

'''num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))
num4 = int(input('Digite um valor: '))

numeros = num1, num2, num3, num4
cont = par = 0
for n in numeros:
    print(f'{n} ', end='')
    if 9 in numeros:
        cont += 1
    if n % 2 == 0:
        par += n
print(f'\nO nove apareceu {cont} vezes.')
print(f'\nO nove apareceu {par} vezes.')
'''

#EX CURSO

num = (int(input('Numero 1 ')),int(input('Numero 2 ')),int(input('Numero 3 ')),int(input('Numero 4 ')))
print(f'Você digitou os valores {num}.')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu {num.index(3)+1}º posião')
else:
    print('O valor 3 não foi encontrado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')