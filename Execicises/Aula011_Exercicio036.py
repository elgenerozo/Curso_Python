"""Exercício 036 - Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
 ou então o empréstimo será negado."""

valor_casa = float(input('Qual o valor do imóvel a ser comprado R$ '))
salario = float(input('Qual é o seu salário R$ '))
anos_financiamento = int(input('Deseja financiar em quantos anos? '))
# limite_prestacao = (salario * 0.30)
ano = 12
val_prest = valor_casa / (anos_financiamento / ano)
if val_prest > salario * 0.30:
    print('Não vai ser possível o financiamento, valor acima de 30% da sua renda mensal')
else:
    print('Seu financiamento foi aprovado.\n' 'Valor total do financiamento R$ {}\n' 'O valor'
          ' mensal da sua parcela será de R$ {}'.format(valor_casa, val_prest))
print('OBRIGADO PELA PREFERENCIA!!!')
