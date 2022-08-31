# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com -5% de desconto.

valor_original = float(input('Entre com o preço do produto R$ '))
valor_desconto = valor_original * 0.05
novo_valor = valor_original * 0.05

print('Valor Original R$ {:.2f}')
print('Valor do desconto R$ {:.2f}'.format(valor_desconto))
print('Novo valor R$ {:.2f}'.format(valor_original - valor_desconto))
