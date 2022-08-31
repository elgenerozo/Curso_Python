# Escreva um programa que converta uma temperatura digitada em °c para °f.

celsius = float(input('Qual a sua temperatura celsius '))
print('Sua temperatura em celsius é {:.2f}°c\n' 'Convertida para fahrenheit é {:.2f}°f'.format(celsius, (celsius*9/5)+32))
