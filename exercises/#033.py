#Faça um programa que leia três números e mostre qual é o maior e qual é of O menor valor é: {menor}.

print('-=-'*20)
n1 = int(input('Adicione o primeiro número: '))
n2 = int(input('Adicione o primeiro segundo: '))
n3 = int(input('Adicione o primeiro terceiro: '))

#EX CURSO
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print(f'O menor valor é: {menor}')

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print(f'O maior número é: {maior}')