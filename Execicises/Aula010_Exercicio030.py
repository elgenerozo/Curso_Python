"""Crei um programa que leia um número inteiro e mostre na tela se ele é par ou impar."""

num = int(input('Digite um numero inteiro: '))
resto = num % 2

if resto == 0:
    print('É um numero par!')
else:
    print('É um numero impar!')
