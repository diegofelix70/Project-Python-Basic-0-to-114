#Desenvolva um programa que leia 6 nuúmeros inteiros e mostre a suam apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


soma = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
print(soma)