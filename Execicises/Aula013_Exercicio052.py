"""
Exercício052 - Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo.
"""
num1 = int(input('Digite um numero inteiro para verificarmos se ele é um número primo ou não: '))

if num1 % num1 == 1 and num1 % 1 == num1:
    for cont in range(10, 0):
        result = num1 % cont
        print(result)
