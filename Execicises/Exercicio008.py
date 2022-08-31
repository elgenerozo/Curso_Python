# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos Dólares ela pode comprar.
# Considere U$$ 1,00 = R$3,23

din = float(input('Quanto dinheiro você tem na carteira: '))
dolar = 3.23
total = din / dolar
print('Você pode comprar U$${:.2f}'.format(total))
