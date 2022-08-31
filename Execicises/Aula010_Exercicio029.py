"""Exercício 029 - Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""

veloc = float(input('Qual a velocidade atual do carro: Km/h '))

if veloc > 80:
    print('Você foi multado!\n''O valor da sua multa é R$ {:.2f}'.format((veloc-80)*7))
else:
    print('Você ainda esta dentro da velocidade permita, mantenha a anteção e boa viagem!')
