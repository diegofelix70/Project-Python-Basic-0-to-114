#Desenvolva im prgorama que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

'''primeiro = int(input('Primeiro Termo: '))
segundo = int(input('Razão: '))

soma = 0
for c in range(primeiro, 10):
    soma += segundo
    print(soma)'''

#EX Curso

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro +(10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end='-> ')
print('ACABOU')