# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual é o seu salário R$ '))
valor_reajuste = salario * 0.15
salario_reajustado = salario + valor_reajuste

print('Seu salário é R$ {:.2f}\n''O valor do reajuste é de R$ {:.2f}\n' 'O valor do seu salário reajustado é R$ {:.2f}'.format(salario, valor_reajuste, salario_reajustado))

