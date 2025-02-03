import math

# Ângulo em graus
angulo_graus = float(input('Adicione o valor a ser convertido: '))

# Convertendo o ângulo para radianos (necessário para as funções trigonométricas)
angulo_radianos = math.radians(angulo_graus)

# Calculando seno, cosseno e tangente
seno = math.sin(angulo_radianos)       # Seno de 45°
cosseno = math.cos(angulo_radianos)    # Cosseno de 45°
tangente = math.tan(angulo_radianos)   # Tangente de 45°

# Exibindo os resultados
print(f"Seno de {angulo_graus}°: {seno:.3f}")
print(f"Cosseno de {angulo_graus}°: {cosseno:.3f}")
print(f"Tangente de {angulo_graus}°: {tangente:.3f}")
