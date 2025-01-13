def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO! \"{entrada}"\ é um preço invalido')
        else:
            válido = True
            return float(entrada)