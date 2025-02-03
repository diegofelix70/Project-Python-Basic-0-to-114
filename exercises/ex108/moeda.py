def metade(num):
    return num / 2

def dobro(num):
    return num * 2

def aumentar(num, porc):
    return num + (porc * (num/100))

def diminuir(num, porc):
    return num - (porc * (num/100))

def moeda(moeda='R$', preco=0):
    return f'{moeda}{preco}'.replace('.', ',')
