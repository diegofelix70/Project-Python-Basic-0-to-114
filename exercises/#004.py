#Faça um programa que leia algo pelo tevlado e mostra na tela o seu tipo primitivo e todas as informações sobre ela.

a = input('Digite algo ')
print('O tipo primitivo desse valor é ', type(a))
#Para ver se é somente espaçosos
print('Só tem espaços?', a.isspace())
#Para ver se tem somente números
print('É um número?', a.isnumeric())
#Alfabético
print('É alfabético? ', a.isalpha())
#Alfanumérico
print('É alfanumérico? ', a.isalnum())
#Maiúscula
print('Está Maiúscula? ', a.isupper())
#Minúscula
print('É Minúscula? ', a.islower())
#Captalaze
print('Está em captalize? ', a.istitle())
