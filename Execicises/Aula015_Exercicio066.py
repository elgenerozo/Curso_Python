"""
EXERCÍCIO066 — Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai para quando o usuário digitar 999, sendo a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
"""
qtd_num_dig = soma = 0

while True:
    num = int(input("Digite um número qualquer e [999 para sair do programa]: "))
    if num == 999:
        break
    qtd_num_dig += 1
    soma += num
print(f"Foram digitados {qtd_num_dig} números, e a soma de todos eles é {soma}")
