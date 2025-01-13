#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''nome = str(input('Digite o sexo [F/M]: '))
while nome != 'm':
    print(nome)
    nome = str(input('Digite um valor: '))
print('Acabou')'''

# Resolução: 
# TRATAMENTO DE STRING:
# Tirar espaços extras: ".strip()" e Deixando tudo em maúscula ".upper", sendo que quer somente a primeira letra, selecionar somente ela "[0]"
# 
# Fica assim no exemplo:
# sexo = str(input('Informe o sexo: [M/F]))".strip.upper[0]"
# while sexo not in 'MmFf:
#   sexo = str(input('Dados inávidos. Novamente: ')).strip().upper()[0]
# print('Sexo: {}').format.(sexo))

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por Favor, tente novamente: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com Sucesso.')