#Faça um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderendo os espaços.

'''frase = input('Digite uma frase para ver ela de trás pra frente: ')

frase.upper()
junto = frase.replace(" ", "")

print(junto.upper())

#Aqui é se eu quiser contar de trás para frente
for c in range(junto): #Tem que fazer a reversão dos números #Acrescenti o -1 para contar reverso
    print('''

#EX Curso

'''frase = input('Digite uma frase para ver ela de trás pra frente: ')

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1): #Vai a até a primeira letra e depois vai voltar um passo negativo. Ele vai pegar o numero e tirar uma, depois vai no -1 porque é menos uma letra e depois vai voltando.
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print(f'Temos um palidromo!')
else:
    print('A frase não é um palindromo!')'''

#Segunda opção

frase = input('Digite uma frase para ver ela de trás pra frente: ')

palavras = frase.split().upper()
junto = ''.join(palavras)
inverso = junto[:: -1]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print(f'Temos um palidromo!')
else:
    print('A frase não é um palindromo!')