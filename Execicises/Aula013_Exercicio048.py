"""Exercicio048 — Faça um programa que calcule a soma entre todos os números
ímpares, que são múltiplos de três e que se encontram no intervalo de 1 até 500."""

soma = 0
for c in range(0, 500):
    soma = soma + 3
print(soma)
