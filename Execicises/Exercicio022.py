"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.

 Ex.: Ana Maria de Souza
 primeiro: Ana
 último: Souza"""

nome = str(input('Digite seu nome completo: ')).strip()
nome_fatiado = nome.split()
print('O seu pimeiro nome é: {}\n' 'O seu último nome é {}'.format(nome_fatiado[0], nome_fatiado.pop()))

# O último nome também pode ser exibido assim

# print('Seu último nome é {}'.format(nome_fatiado[len(nome_fatiado)-1]))  --> corrigir
