"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
 EX.:
Digite um número : 1834
    unidade: 4
    dezena: 3
    centena: 8
    milhar: 1
"""

num = int(input('Entre com um numero inteiro qualquer que esteja entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o numero: {}\n' 'Unidade: {}\n' 'Dezena: {}\n' 'Centena: {}\n' 'Milhar: {}'.format(num, u, d, c, m))




