dezoito = mulheres = homens = 0

while True:
    sexo = continuar = ' '

    print('-'*30)
    print('    CADASTRE UMA PESSOA')
    print('-'*30)

    idade = int(input('Idade? '))
    if idade >= 18:
        dezoito += 1 #contador mais dezoito

    while sexo not in 'MF': # Dentro de um while para me entregar somente se digitado M ou F
        sexo = str(input('Sexo? [M/F] ')).strip().upper() [0]
    if 'M' in sexo: #contador de homens
        homens += 1
    if 'F' in sexo and idade<20:
        mulheres += 1 #contador de mulhers + menor de 20

    print('~'*30)
    while continuar not in 'SN': # Dentro de um while para me entregar somente se digitado S ou N
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    if continuar == 'N':
        break

print(f'\nTotal de pessoas com mais de 18 anos: {dezoito}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} com menos de 20 anos')

