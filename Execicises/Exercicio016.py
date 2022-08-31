"""Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo."""
from math import cos, tan, sin, radians

angulo: float = float(input('Entre com um numero: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O numero digitado foi {:.2f}\n' 'O cosseno dele é {:.2f}\n' 'A tangente dele é {:.2f}\n' 'O seno dele é {:.2f}'.format(angulo, cosseno, tangente, seno))
