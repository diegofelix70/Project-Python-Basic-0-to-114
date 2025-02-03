# Sou seu computador...
# Acabei de pensar em um número de 0 a 10.
# Será que você consegue adivinhar qual foi?
# Qual é o seu palpite?.

'''import random
aleatorio = random.randint(1, 10+1)
print(aleatorio)'''

'''import random

aleatorio = random.randint(1, 10+1)
digita = float(input('Estou pensando em um número de 0 a 10. Você consegue adinhar? Qual é o seu palpite? '))
print(f'O numero foi: {aleatorio}')'''

import random

aleatorio = random.randint(1, 10+1)
digita = float(input('Estou pensando em um número de 0 a 10. \n Você consegue adinhar? \n Qual é o seu palpite? '))
while digita != aleatorio:
    digita = int(input('Hum... ainda não foi dessa vez. Digite novamente: '))
print('Parabéns! Estava pensando nesse exato número.')