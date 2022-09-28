"""
Exercício065 — Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior
e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
não continuar a digitar valores.
"""

resp = "S"
soma = media = qtd_val = maior = menor = 0

while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    qtd_val += 1
    if qtd_val == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / qtd_val
print(f"Soma total dos valores {qtd_val}")
print("A média dos valores é: {}".format(media))
print(f"Maior número {maior}, e o menor numero {menor}")
print("Acabou")
