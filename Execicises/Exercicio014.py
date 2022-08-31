"""Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porcão inteira.
Digite um número: 6.127 e tem a parte inteira 6"""

from math import trunc
num = float(input('Entre com um numero inteiro:'))
print('O numero digitado foi {}\n''E sua parte inteira é {}'.format(num, trunc(num)))

# Outra maneira de se fazer o exercio, logo abaixo:
print('O numero digitado foi {}\n''E sua parte inteira é {}'.format(num, int(num)))
