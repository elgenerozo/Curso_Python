"""Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa."""

from math import hypot, degrees

cat_op = float(input('Entre com o valor do cateto oposto: '))
cat_adj = float(input('Entre com o valor do cateto adjacente: '))
#degrees(cat_op)
#degrees(cat_adj)

print('O comprimento da hipotenusa é: {:.2f}'.format(hypot(cat_op, cat_adj)))
