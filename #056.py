#Desenvolva um programa que leia o NOME, IDADE E SEXO de 4 pessoas. No final do programa, mostre:
#Primeiro programa do Gabriel e Diego juntos.
mais_velho=''
soma= 0
cont = 0
maior = menor = 0

for c in range(1, 3):
    nome = input(f'nome da {c}ª pessoa: ')
    idade = int(input(f'idade da {c}ª pessoa: '))
    soma+=idade 
    sexo = str(input(f'sexo da {c}ª pessoa: ')).upper()

    if 'F' in sexo and idade<20:
        cont += 1 #contador de mulhers
    if 'M' in sexo and nome:
        if idade == 1:
            maior = menor = idade
        else:
            if idade > maior:
                maior = idade
                mais_velho = nome
            if idade < menor:
                menor = idade
print(f' A nwdia de idade do crupo é de {soma/2}')
print(f' O homem mauis velho tem {maior} anos e se chama {mais_velho}')
print(f'Ao todo sao {cont} mulheres com menos de 20 anos')
    


