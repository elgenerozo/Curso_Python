"""
Exercício059 — Crie um programa que leia dois valores e mostre um menu na tela:

[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Números
[5]Sair do Programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

#   Declaração das variáveis globais


#   Solicita as duas entradas necessárias (num1, num2)
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o primeiro numero: "))

#   Declara as varíaveis globais
soma = num1 + num2
mult = num1 * num2
novo_num = int
sair = str
maior = float

#   Define o maior numero entre num1 e num2
if num1 > num2:
    maior = num1
else:
    maior = num2

#   Definindo o menu de opções.
menu = {"[1] - Somar": soma,
        "[2] - Multiplicar": mult,
        "[3] - Saber Maior": maior,
        "[4] - Digitar Dois Novos Numeros": novo_num,
        "[5] - Sair do Programa": sair
        }

#   Imprime o menu
opcoes = int(input("[1] - Somar\n""[2] - Multiplicar\n""[3] - Saber Maior\n""[4] - Digitar Dois Novos Numeros\n"
                   "[5] - Sair do Programa\n""Escolha uma das opções acima: "))
#   Soma os dois termos num1 + num2
if opcoes == 1:
    print("O resultado da soma é {}".format(menu["[1] - Somar"]))

#   Multiplica os dois termos num1 * num2
if opcoes == 2:
    print("A multiplicação dos dois termos é {}".format(menu["[2] - Multiplicar"]))

#   Identificando o maior número entre num1 e num2. ---> REVISAR, POIS ESTA MOSTRANDO A SAIDA JUNTO COM O INTEM 4.
if opcoes == 3:
    print("O maior número entre os dois é {}".format(menu["[3] - Saber Maior"]))
else:
    print("O maior número entre os dois é {}".format(menu["[3] - Saber Maior"]))

#   Solicita novamente os dois numeros (num1 e num2) ---> FALTA TERMINAR
if opcoes == 4 and novo_num:
    num1 = float(input("Digite novamente o primeiro número: "))
    num2 = float(input("Digite novmente o segundo número: "))

#   Fecha e sai da aplicação
if opcoes == 5:
    print("Programa Finalizado...")
