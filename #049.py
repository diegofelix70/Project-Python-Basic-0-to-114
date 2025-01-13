#Refaça o DESAFIO #009, mostrando a tabuada de um número que o usuário escolher, só que agora usando o laço for

numero = int(input('Adicione um número para ver a sua taboada: '))

soma = 0
cont = 0
for tabuada in range(1,11):
    soma = tabuada * numero
    cont += 1
    print(f'{numero} x {cont} = {soma}')

#EX Curso

num = int(input('Digite um número para ver a tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num*c}') #Psso colocar para fazer a operação dentro das chaver também.