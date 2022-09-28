"""
Exercício060 — Faça um programa que leia um número qualquer e mostre o seu fatorial.
(TENTAR FAZER COM O "FOR" TAMBÉM).

Ex.: 5! = 5x4x3x2x1=120
"""
from math import factorial

num = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(num)
print(f"O fatorial de {num} é {f}.")

print("==*" * 30)

"Outra modo como ser feito"

num = int(input("Digite um número para calcular seu fatorial: "))
cont = num
f = 1
print(f"Calculando {num}!")
while cont > 0:
    print(f"{cont}", end=" ")
    print(f" X " if cont > 1 else f"= {f}", end=" ")
    f *= cont
    cont -= 1

