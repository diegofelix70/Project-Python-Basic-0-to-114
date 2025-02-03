#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

# Entrada dos valores dos catetos
cateto_oposto = float(input("Informe o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Informe o comprimento do cateto adjacente: "))

# Cálculo da hipotenusa
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

# Exibição do resultado
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")
