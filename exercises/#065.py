#Crie um programa que leia vários numeros inteiros pelo teclado no final da execução mostre a media de toda a execução, mostre a média enmre todos os valores e qual fo o maior e o menor valores lidos. O p´rograma deve perguntar ao usuario se ele quer ou nmão continuar a digitar valores.

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1

    # if quant == 1:
    #     maior = menor = num
    # else:
    #     if num > maior:
    #         maior = num
    #     if num < menor:
    #         menor = num
            
    maior=max(num)
    menor=min(num)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip() [0]

media = soma / quant
print(f'Você digitou {num} e a média foi {media:.2f}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')