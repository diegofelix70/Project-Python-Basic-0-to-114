from ex108 import moeda

p = float(input('Digite um número: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Aumentando 13%, temos {moeda.diminuir(p, 13)}')