# Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi algado. Calcule o preço
# a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
valor_km = 0.15
dia_carro = 60
km_percorrido = float(input('Qual a quantidade de KM percorrido: '))
dia_alugado = int(input('Quantos dias foi alugado: '))
print('Total a pagar R$ {:.2f}'.format((dia_alugado*dia_carro)+(valor_km*km_percorrido)))


