"""
Exercício057 — Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" e "F".
Caso esteja errado, peça a digição novamente até ter um valor correto.
"""


"""******************************  OUTRA MANEIRA DE SER FEITO  *******************************
        while True:
        cont = input("Digite o sexo: F/M  ")

        while cont not in ("F", "M"):
                cont = input("Escolha F/M > ")

        if cont == "N":
                print("Break")
        break
******************************************************************************************"""

escolha = input("Digite o Sexo F/M: ").strip().upper()[0]

while escolha not in ("F", "M"):
        escolha = input("Digite o Sexo Corretamente F/M: ").strip().upper()[0]
else:
        print("It's over!!!")
