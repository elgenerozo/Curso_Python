"""
Exercício063 — Escreva um programa que leia um número n inteiro qualquer e mostre na
tela os n primeiro elementos de uma Sequência de Fibonacci.

Ex:
0 -->1 -->1 -->2 -->3 -->5 -->8

O que e uma sequência Fibonacci?

Na matemática, os números de Fibonacci são uma sequência ou sucessão definida como recursiva pela
fórmula: F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1 . Os primeiros números de
Fibonacci são: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765
"""

num = int(input("Quantos termos deseja mostrar? "))

t1 = 0
t2 = 1
cont = 3

print(f"{t1} --> {t2}", end=" ")

while cont <= num:
    t3 = t1 + t2
    print(f" --> {t3}", end=" ")
    t1 = t2
    t2 = t3
    cont += 1

print("FIM!")
