"""
Exercício061 — Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura "while".
*********************************************************************************************
Exercício051 — Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.

 FORMULA P.A.:
   an = a1+(n-1)r
   an = termo geral
   a1 = primeiro termo
   n = posição do termo geral
   r = razão da P.A
*********************************************************************************************
"""
print("Gerador de P.A")
print("-=" * 30)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da P.A: "))
termo = primeiro
cont = 1

while cont <= 10:
    print(f"{termo} --> ", end=" ")
    termo += razao
    cont += 1
print("FIM!")
