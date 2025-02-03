#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

'''print('Gerador de PA')
print('-='*10)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1
quant = 10
opcao = 0
while opcao != 0:

     while cont <= 10:
        print(f'{termo} ->', end='')
        termo += razão
        cont += 1
if opcao == 10:
    novo = int(input('\nDeseja mais quantos termos? '))

print('fim')'''

print('Gerador de PA')
print('-='*10)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1

#NOVOS
total = 0
mais = 10

while mais != 0:
    total = total + mais #Sempre se começa com os parametros que você deseja começar, depois, já dentro da variavel, você colocar para esse parametro receber os novos valores.
    while cont <= total:
        print(f'{termo} ->', end='')
        termo += razão
        cont += 1 
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? ')) #Dessa forma eu não preciso colocar um if, somente subo para fazer uma nova atualização.
print('FIM')
print(f'Progressão finalizada com {total} termos mostrados')