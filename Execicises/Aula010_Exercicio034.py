"""Faça um programa que leia o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.200,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%."""

sal = float(input('Digite o valor do seu salário R$ '))


if sal > 1200:
    val10 = ((sal * 0.10) + sal)
    print(val10)
else:
    val15 = ((sal * 0.15) + sal)
    print(val15)
print('Reajuste Efetuado!')
