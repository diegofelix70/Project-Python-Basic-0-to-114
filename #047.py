#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 50.

#Tradicional
'''for i in range(0, 5+1, 2):
    print(i)
print('Fim')'''



#MELHOR FORMA
#Para deixar um no lado do outro
for i in range(0, 50+1, 2):
    print(i, end=' ')
print('Fim')

#Usando o if
'''for i in range(1,50+1):
    if i % 2 ==0:
        print(i, end=' ')'''