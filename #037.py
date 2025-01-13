#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 Para Binário
#2 Para Octal
#3 Para Hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha um número para converção
      [1] converter para BINÁRIO)
      [2] converter para OCTAL)
      [3] converter para HEXADECIMAL''')
opção = int(input('Escolha uma das opções: '))
if opção == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)}')
elif opção == 2:
    print(f'{num} convertido para Binário é igual a {oct(num)}')
elif opção == 3:
    print(f'{num} convertido para Binário é igual a {hex(num)}')
else:
    print('Opção invalida, tente novamente!')