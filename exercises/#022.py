frase = str(input('Qual é o seu nome? ')).strip()#Se coloca .strip no começo já para eliminar todos os espaços no começo e no fim.


print('Seu nome em maiúscula é {}'.format(frase.upper()))
print('Seu nome em minúscula é {}'.format(frase.lower()))
print('Seu nome tem ao todo {} letras'.format(len(frase) - frase.count(' ')))
#print('A primeira letra tem {} letras.'.format(frase.find(' ')))
#Para encontrar contar uma palavra dentro da frase, basta dividi-lá em uma frase e usar a linsta para contar.
lista = frase.split() #Primeiro é criando uma função para ela.
print(lista)
print('A primeira palavra tem {} letras.'.format(len(lista[1])))