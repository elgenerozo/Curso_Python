# ex.006_A - Crie um algoritimo que leia um número e mostre seu dobro, triplo e a raiz quadrada.

from math import sqrt

num = float(input('Entre com o valor a ser calcudo: '))

print(' O numero digitado foi: {}\n'.format(num), 'O seu dobro é: {}\n'.format(num*2), 'E sua raiz quadrada é: {}'.format(sqrt(num)))
