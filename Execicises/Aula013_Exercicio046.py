"""Exercicio046 - Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1s entre eles.
E depois mostre um emogi de fogos estourando."""
from time import sleep
import emoji


for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize('Python is ::performing_arts:'))
