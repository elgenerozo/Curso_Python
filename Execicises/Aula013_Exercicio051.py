"""Exercício051 — Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

""" FORMULA P.A.:
   an = a1+(n-1)r
   an = termo geral
   a1 = primeiro termo
   n = posição do termo geral
   r = razão da P.A
 """
primeiro_a1 = int(input('Digite o primeiro termo: '))
razao_r = int(input('Digita a razão da P.A.: '))
num_elem_n = int(input('Quantos elementos deseja exibir: '))

ultimo = primeiro_a1 + (num_elem_n - 1) * razao_r
for cont in range(primeiro_a1, ultimo, razao_r):
    print(cont)
"""    if primeiro_a1 < 0:
        for cont in range(primeiro_a1 - 1, ultimo, razao_r):
            print(cont)
"""
print('Essa foi a demonstração da P.A.')
