'''Quantos dias alugado e quantos km rodados'''

dias = int(input('quantos dias rodados: '))
km = float(input('quantos km rodados: '))

valordia = 60
valorkm = 0.15

aluguel = (dias * valordia) + (km * valorkm)

print(f'o valor do aluguel fica em: R${aluguel:.2f}')