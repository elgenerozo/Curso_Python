"""
Exercício067 — Faça um programa que mostre a tabuada de vários números, um de cada
vez, para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.
"""
produto = num = 0

while True:
    cont = 0
    num = int(input("Digite o número: "))
    if num < 0:
        break
    while cont <= 10:
        produto = num * cont
        print(f"{num} X {cont} = {produto}")
        cont += 1
print("Programa finalizado!")
