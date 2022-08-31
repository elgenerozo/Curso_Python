"""Faça um programa que leia 3 numero e mostre qual é o maior e o menor."""
n1 = int(input('Entre com o primeiro numero: '))
n2 = int(input('Entre com o segundo numero: '))
n3 = int(input('Entre com o terceiro numero: '))

# Verificando quem é o maior
maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
else:
    print('Maior {}'.format(maior))

    # Verificando quem é o menor
    menor = n3
    if n2 < menor:
        menor = n2
    if n1 < menor:
        menor = n1
    else:
        print('Menor {}'.format(menor))

