"""
Exercício053 — Crei um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços e acentos.

Ex.: Apos a sopa.
     A sacada da casa.
     A torre da derrota.
     O lobo ama o bolo.
     Anotaram a data da maratona.
"""

frase = str(input('Digite uma frase: ')).strip()
print(frase.rstrip())
