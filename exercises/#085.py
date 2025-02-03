num = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valor PARES digitados foram: {num[0]}')
print(f'Os valor ÍMAPARES digitados foram: {num[1]}')