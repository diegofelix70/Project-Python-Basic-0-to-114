#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. Ni final, mostre quantos numeros foram digitados e qual foi a soma entre elkes (desconsidernado o flag)

numero = cont = soma = 0

while True: #Colocar o recebedor de números por último, assim quando der 999 não vai somar, porque vai sair da contagem.
    numero = int(input('Digite um número [999 para parar] ')) #Com o True, já se inicia verdadeiro, sem a necessidade de dar um valor 0 fora da chave.

    if numero == 999:
        break    
    cont += 1
    soma += numero

print(f'Você digitou {cont} números e a soma entre eles é de {soma}.')