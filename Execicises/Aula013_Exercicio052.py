"""
Exercício052 - Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo.
"""
num1 = int(input('Digite um numero inteiro para verificarmos se ele é um número primo ou não: '))

tot = 0
for c in range(1, num1+1):
    if num1 % c == 0:
       print('\033[33m', end='')
       tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end='')
print(f'\n\033[mO Numero {num1} foi divisivel {tot} vezes.')
if tot == 2:
    print('E por isso é um numero PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
