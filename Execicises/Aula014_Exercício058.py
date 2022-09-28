"""Exercício058 — Melhore o jogo do Desafio 028, onde o computador vai "pensar" em um número entre 0 e 10.
Contúdo agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.
"""
from random import randint

escolha = int
cont = 0
comp = randint(0, 10)
print(comp)
#   Apenas mostra a jogada do computador.
#   print(comp)

while escolha != comp:
    escolha = int(input("Digite seu numero: "))
    cont += 1
else:
    print(f"Você acertou!!! O número é {escolha}, você precisou de {cont} jogadas!")
