"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagem de até 200,00Km e
R$0,45 para viagens mais loingas."""

dist = float(input('Qual as distância da viagem em KM? '))

if dist <= 200:
    print('Para viagens até {}km, o valor cobrado por km é {}, e sua passagem custará R$ {:.2f}'.format(dist, 0.50, dist * 0.5))
else:
    print('Para viagens acima de {} km, o valor cobrado por km é {}, e sua passagem custará R$ {:.2f}'.format(dist, 0.45, dist * 0.45))
