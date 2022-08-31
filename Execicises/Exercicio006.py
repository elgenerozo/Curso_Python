# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

metro = float(input('Entre com a medida: '))
centimetro = metro * 100
milimetro = metro * 1000
print('A medida digitada foi {}'.format(metro))
print('Medida convertida para metros {:.2f}cm\n''Medida convertida para milimetro {}mm'.format(centimetro, milimetro))


