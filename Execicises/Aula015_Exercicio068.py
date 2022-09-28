"""
Execício068 — Faça um programa que jogue par ou ímpar com o computador. O jogo
só será interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
"""
from random import randint

vitorias = int
comp = int
qtd_vit = 0

while True:
    num = int(input("Diga um valor: "))
    escolha = str(input("Par ou Ímpar? [P/I] ")).upper().strip()[0]
    print(escolha)
    comp = randint(0, 10)
    print(comp)

    if (num + comp) % 2 != 0:
        print(f"Você jogou {num} e o computador {comp}. \nTotal de {num + comp}. Ímpar venceu!")
    else:
        print(f"Você jogou {num} e o computador {comp}. \nTotal de {num + comp}. Par venceu!")
