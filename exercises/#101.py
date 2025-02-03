# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGPATÓRIO nas eleições.
'''from datetime import date 

def voto(ano):
    idade = date.today().year - ano

    if idade <= 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif idade == 16 or idade == 17:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')

ano = int(input('Qual é o seu ano de nascimento:  '))

voto(ano)
'''

# EX Curso

def voto(ano):
    from datetime import date # Se importa dentro da def para economizar espaço de memória
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.' # desde que eu coloque a def dentro de um print não tem problema só inicar o texto que vai ser mostrado entre aspas.

nasc = int(input('Qual é o seu ano de nascimento:  '))
print(voto(nasc))