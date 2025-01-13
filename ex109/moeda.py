def metade(num, formato=False):
    res = num / 2
    return res if formato is False else moeda(res)

def dobro(num, formato=False):
    res = num * 2
    return res if formato is False else moeda(res) # Chamar a função "moeda" # se usa "res" para chamar a resposta ser formatoada

def aumentar(num, porc, formato=False):
    res = num + (porc * (num/100))
    return res if formato is False else moeda(res)

def diminuir(num, porc, formato=False):
    res = num - (porc * (num/100))
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda='R$', formato=False):
    res = f'{moeda}{preco:>.2f}'.replace('.', ',')
    return res if formato is False else moeda(res)

'''def resumo(num, aumento, redução):
    txt = '   RESUMO DO VALOR'
    tam = len(txt) + 6
    print('-' * tam)
    print(txt)
    print('-' * tam)
    print(f'Preço analisado: ', end='')
    print(f'{moeda(num)}')
    print(f'Dobro do Preço: ', end='')
    print(f'{dobro(num)}')
    print(f'Metade do Preço: ', end='')
    print(f'{metade(num)}')
    print(f'{aumento}% de aumento: ', end='')
    print(f'{aumentar(num, aumento)}')
    print(f'{redução}% de redução: ', end='')
    print(f'{diminuir(num, redução)}')''' 

# EX CURSO



def resumo(preço, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30)) #Definindo o valor de caracteres e centralizando.
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do Preço: \t{dobro(preço, True)}')
    print(f'Metade do Preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
                
