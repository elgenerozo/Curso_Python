"""Exercício056 — Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
— A média de idade do grupo.
— Qual é a idade do homem mais velho.
— Quantas mulheres tem menos de 20 anos."""

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ""
tot_idade_mulher = 0
qtd_idade_mulher_menor21 = 0


for p in range(1, 5):
    print(f"---------{p}ª PESSOA---------")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma_idade += idade

    if p == 1 and sexo in "Mm":
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in "Mm" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in "Ff" and idade < 20:
        tot_idade_mulher = idade
        qtd_idade_mulher_menor21 += 1

media_idade = soma_idade / 4

print(f"A média de idade do grupo é {media_idade} anos.")
print(f"O Sr.{nome_velho} é homem mais velho, com {maior_idade_homem} anos.")
print(f"Nesse grupo temos um total de {qtd_idade_mulher_menor21} menores que 21 anos.")
