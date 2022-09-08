"""
Exercício054 — Crei um programa que leia o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda não atingiram a maioridade(>21anos) e
quantas já são maiores.
"""
from datetime import date

#   Convertendo atual como data valida.
atual = date.today().year

tot_maior = 0
tot_menor = 0

#   Contador de 1 - 7.
for c in range(1, 8):
    nasc = int(input('Entre com ano de nascimento: '))
#   Calculando a idade do usuário.
    idade = atual - nasc
#   Se o ano digitado for maior que o ano atual, será considerado uma data inválida.
    if nasc > atual:
        print('Data de nascimento invalida, tente novamente!')
#   Se a idade for maior o igual a 21 anos, vai somar um usuário a variável tot_maior.
    if idade >= 21:
            tot_maior += 1
#   Se a idade for menor que 21 anos, vai somar um usuário a variável tot_menor.
    else:
            tot_menor += 1
#   Imprime na tela o total de menores e maiores.
print(f"Essa é a quantidade {tot_menor} de pessoas menores. Essa é a quantidade {tot_maior} de pessoas maiores de idade.")




