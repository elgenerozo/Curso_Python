"""
Exercício059 — Crie um programa que leia dois valores e mostre um menu na tela:

[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do Programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o primeiro número: "))

soma = num1 + num2
multiplicacao = num1 * num2
opcao = 0

while opcao != 5:

    print("[1] - Somar")
    print("[2] - Multiplicar")
    print("[3] - Maior")
    print("[4] - Novos Números")
    print("[5] - Sair do Programa")
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        print("A soma dos dois números é: {}".format(soma))
    elif opcao == 2:
        print("A multiplicação dos dois números é: {}".format(multiplicacao))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
            print("Entre os dois termos o maior é: {}".format(maior))
        else:
            maior = num2
            print("Entre os dois termos o maior é: {}".format(num2))
    elif opcao == 4:
        print("Digite os dois números novamente.")
        num1 = int(input("Digite o primeiro número nomvamente: "))
        num2 = int(input("Digite o primeiro número nomvamente: "))
    elif opcao == 5:
        print("Finalizando...")
        print("Opção inválida. Tente novamente!")
    print("=*=" * 20)
print("Fim do programa!")
