"""
Exercício060 — Faça um programa que leia um número qualquer e mostre o seu fatorial.
(TENTAR FAZER COM O "FOR" TAMBÉM).

Ex.: 5! = 5x4x3x2x1=120
"""

num = int(input("Digite o numero do fatorial: "))
total = num * (num - 1)
print(total)
num = num - 2
for num in range(num, 1):
    total = total * num
    print(total)
    num = num - 1
    total = total * num

print("ok")