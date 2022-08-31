"""Exercicio050 — Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""

soma = 0
for cont in range(0, 6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma + num
    elif num % 2 != 0:
        print(soma)
print(f'A soma total dos numeros pares é {soma}')
