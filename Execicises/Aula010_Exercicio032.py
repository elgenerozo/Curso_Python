"""Faça um programa que leia um ano qualquer e mostre se ele é um ano bissexto."""
from datetime import date

ano = int(input('Digite o ano que deseja analisar, ou coloque o número 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano {} É BISSEXTO!'.format(ano))
else:
    print('Esse NÃO é um ano {} BISSEXTO'.format(ano))
