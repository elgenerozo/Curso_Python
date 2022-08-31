"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
 lendo o nome deles e escrevendo o nome do escolhido."""
from random import choice

n1 = str(input('Entre com o primeiro nome: ')).split()
n2 = str(input('Entre com o segundo nome: ')).split()
n3 = str(input('Entre com o terceiro nome: ')).split()
n4 = str(input('Entre com o querto nome: ')).split()

lista_nomes = [n1, n2, n3, n4]

print('O nome escolhido é: {}'.format(choice(lista_nomes)))
