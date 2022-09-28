"""
Exercício064 - Crie um programa qe leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
 digitar o valor 999, sendo a condição de parada. No final mostre quantos números foram digitados e qual dou a soma
 entre eles.

(desconsiderando o flag).
"""
num = int
contador = 0
somador = 0

while num != 999:
    num = int(input("Digite um número inteiro: "))
    contador = contador + 1
    somador = somador + num
    if num == 999:
        print(f"Foram efetuadas {contador - 1} interações.")
        print(f"A soma de todos os números digitados é {somador - 999}.")
        print("Saindo")
print("Finalizando...")
