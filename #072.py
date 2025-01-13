#Um programa onde a pessoa digita um numero de 0 a 20 e o computador escreve ele por extenso

numero = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'


while True:
    choice = int(input('Escolha um número de 0 a 20 '))
    if 0 <= choice <=20:
        break
    print('Tente novamente...', end='')
    
print(f'Você digitou o número {numero[choice]}')
