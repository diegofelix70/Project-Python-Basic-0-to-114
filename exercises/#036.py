#Escreva um programa para aprovar o empréstimo bancário para a cp,ra de im,a casa. O programa vai perguntar o valor da casa, o salário do comprador r em quantos anos eaa vai pagar
# Calcule o valor da prestação mesnal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


#VC = Valor da Casa
#QA = Quantidade de anos que vai pagar
#QM = Quantidade Mês
#VM = Valor mês
#SL = Salário
#porcent = Porcentagem salário

vc = float(input('Qual valor da casa? '))
qa = float(input('Quantidade de anos que preptende pagar? '))
sl = float(input('Qual é o salário? '))

qm = (vc / qa) / 12
porcent = (sl / 100) * 30

if porcent >= qm:
    print('Tem direito')
else:
    print('Não tem direito.')