'''

cont = 1

#NOVOS
total = 0
mais = int(input('Qauntos termos você quer mostrar? '))
termo = mais

total = total + mais #Sempre se começa com os parametros que você deseja começar, depois, já dentro da variavel, você colocar para esse parametro receber os novos valores.
while cont <= total:
    print(f'{termo} ->', end='')
    termo += 1
    cont += 1 
print('FIM')'''

print('-'*30)
print('Sequencia de fibonacci')
print('-'*30)

n = int(input('Quantos termos você vai querer mostrar? '))

t1 = 0
t2 = 1

print('~'*30)
print(f'{t1} -> {t2}', end='')

cont = 3
while cont <= n:
    t3 = t1 +  t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont +=1
print('fim')
