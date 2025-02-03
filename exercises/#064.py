#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

'''numero = int(input('Digite um número [999 para parar] '))

cont = 0
c = 0
soma = 0

while numero != 999:
    numero = numero
    cont += 1
    soma += numero
    
fim = soma - 999
print(f'Terminou com você digitando {cont} e a soma deles foi de {fim}.')'''

#EX CURSO
numero = cont = soma = 0
numero = int(input('Digite um número [999 para parar] '))

while numero != 999: #Colocar o recebedor de números por último, assim quando der 999 não vai somar, porque vai sair da contagem.
    cont += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar] '))

print(f'Você digitou {cont} números e a soma entre eles é de {soma}.')