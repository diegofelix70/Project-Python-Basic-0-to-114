palavras = 'bolacha', 'abacaxi', 'pirâmide', 'oceano', 'girassol', 'planeta', 'geladeira', 'livro', 'bicicleta', 'caminho', 'travesseiro', 'morango', 'galaxia', 'foguete', 'amarelo', 'relogio', 'nuvem', 'estrela', 'borboleta', 'montanha'

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')