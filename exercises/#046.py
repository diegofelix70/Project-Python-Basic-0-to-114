import time #Se usa o importe para importar a biblioteca.

def contagem_regressiva():
  for i in range(10, 0, -1):
    print(i)
    time.sleep(1) #TEm que ir buscar a importação do time
                  #Usa-se o "."(ponto) para chamar uma função específica, que no caso é o "sleep".
  print("Feliz Ano Novo!")

contagem_regressiva()