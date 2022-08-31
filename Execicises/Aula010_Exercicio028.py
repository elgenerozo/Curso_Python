"""Exercício 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual é o número escolhido pelo computador.

- O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep
num = randint(0, 5)
# print(num)
num_user = int(input('Tente advinhar o numero que o computador gerou: '))
print('PROCESSANDO...')
sleep(5)
if num == num_user:
    print('Acertou DISGRAMADO')
else:
    print('Errou!')
    