"""Exercicio 044 - Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu "preço normal" e "Condição de Pagamento":

- À vista dinheiro/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros."""

preco_normal = float(input('Qual é o preço do produto R$ '))

a_vista = (preco_normal - (preco_normal * 0.10))
a_vista_cartao = (preco_normal - (preco_normal * 0.5))
duas_cartao = a_vista_cartao
tres_cartao = (preco_normal + (preco_normal * 0.20))

preco_calculado = {'A Vista': a_vista,
                   'A Vista Cartão': a_vista_cartao,
                   'Duas Vezes Cartão': duas_cartao,
                   'Três Vezes no Cartão': tres_cartao}

opcao = str(input('Tecle a forma de pagamento: \n A Vista \n A Vista no Cartão \n '
                  'Duas Vezes no Cartão \n Três Vezes no Cartão \n'))
if opcao == 'A Vista':
    print('A forma de pagamento escolhida foi A Vista, e o valor é R${:.2f}'
          .format(preco_calculado['A Vista']))
elif opcao == 'A Vista Cartão':
    print('A forma de pagamento escolha foi A Vista no Cartão, e o valor é R${:.2f}'
          .format(preco_calculado['A Vista Cartão']))
elif opcao == 'Duas Vezes no Cartão':
    print('A forma de pagamento escolhida foi Duas Vezes no Cartão, e o valor é R${:.2f}'
          .format(preco_calculado['Duas Vezes Cartão']))
elif opcao == 'Três Vezes no Cartão':
    print('A forma de pagamento escolhida foi Três Vezes no Cartão, e o valor é R${:.2f}'
          .format(preco_calculado['Três Vezes no Cartão']))
else:
    print('Opção inválida')
