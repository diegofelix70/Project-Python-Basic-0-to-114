#Determine se o ano é Bissexto

ano = int(input('Digite um ano para saber se ele é Bissexto: '))

"""bissexto = ano % 4 
if bissexto == 0:
    print(f'O ano {ano} é Bissexto.')
else:
    print(f'O ano {ano} não é Bissexto')"""
 
#EX PROFESSOR
#Primeiro eu posso adicionar tudo dentro do if instrução

from datetime import date # Aqui vai se puxar a nossa data atual

if ano == 0: #Aqui eu quero colocar uma condição para se caso a pessoa quiser ver a data de hoje.
    ano = date.today().year # Esse ponto today() vai pegar o dia de hoje. Esse year vai ignorar o restante pegando somente o ano.
if ano % 4 == 0 and ano % 100 or 400 == 0:
    print(f'O ano {ano} é Bissexto.')
else:
    print(f'O ano {ano} não é Bissexto')

