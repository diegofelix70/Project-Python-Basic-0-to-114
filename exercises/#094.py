'''cadastro = dict()
dados = list()

while True:
    cadastro.clear()
    keep = ' '

    cadastro['Name'] = str(input('Nome: '))
    cadastro['gener'] = str(input('sexo: '))
    cadastro['age'] = int(input('idade: '))
    dados.append(pessoas.copy())
    
    if keep not in 'SN':
        keep = str(input('Deseja continuar? '))
    else:
        break
print(dados)'''

galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexto'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexto'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    


    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda somente S ou N.')
    if resp == 'N':
        break
print('-=-'*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=())
print()
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')