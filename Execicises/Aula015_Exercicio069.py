"""
Crie um pragrama que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o pragrama deverá perguntar se
o usuário quer ou não continuar.
No final mostre:

A — quantas pessoas tem mais de 18 anos.

B — quantos homens foram cadastrados.

C — Quantas mulheres tem menos de 20 anos.

"""
qtd_pessoas_18_mais = qtd_homem = qtd_mulheres_20_menos = 0

while True:
    nome = str(input("Digite o nome: ")).strip()
    idade = int(input("Digite o idade: "))
    sexo = str(input("Digite o sexo [M/F]: ")).upper().strip()[0]
    if sexo in "MF" != "MF":
        sexo = str(input("Digite CORRETAMENTE o sexo [M/F]: ")).upper().strip()[0]
    if idade > 18:
        qtd_pessoas_18_mais += 1
    if sexo in "M":
        qtd_homem += 1
    if sexo in "F" and idade < 20:
        qtd_mulheres_20_menos += 1
    continuar = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
    if continuar in "S""N" != "S""N":
        continuar = str(input("Digite CORRETAMENTE!." "Deseja continuar? [S/N]: ")).upper().strip()[0]
    if "N" == continuar:
        break
print(f"Quantidades de pessoas maiores de 18 anos {qtd_pessoas_18_mais}.")
print(f"Quantidades de homens cadastrados {qtd_homem}.")
print(f"Quantidades de mulheres menores de 20 anos {qtd_mulheres_20_menos}.")
print("PROGRAMA FINALIZADO")
