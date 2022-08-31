"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
elas podem ou não formar um triângulo."""

r1 = float(input('Entre com o comprimento da primeria reta: '))
r2 = float(input('Entre com o comprimento da Segunda reta: '))
r3 = float(input('Entre com o comprimento da terceira reta: '))

r_mair = r1

if (r2 + r3) >= r_mair:
    print('É um triangulo retangulo')
else:
    print('Não é')
