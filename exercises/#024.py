cid = str(input('Em que cidade vocÊ nasceu? ')).strip().upper()
#print(cid[:5].upper() == 'SANTO') #Mudando para evitar erros
#cidade = cid.upper() #Adicionado na String
resultado = 'SANTO' in cid
print(resultado)
