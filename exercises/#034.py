#Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários speriores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

antes = float(input('Adicione o valor do funcionário: R$ '))

atualMenor = (antes / 100) * 15
atualMaior = (antes / 100) * 10

"""if antes <= 1250:
    salario = antes + atualMenor
else:
    salario = antes + atualMaior"""

#EX CURSO
if antes <= 1250:
    salario = antes  + (antes * 15 / 100)
else:
    salario = antes  + (antes * 10 / 100)


print(f'O valor atual do funcionário vai ser de R${salario}.')