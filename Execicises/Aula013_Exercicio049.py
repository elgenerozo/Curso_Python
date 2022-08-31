"""Exercico049 - Refaça o desafio009, mostrando a tabuada de um número que o usuário escolher,
contudo agora ultilizando o laço for."""

num_escolhido = int(input('Digite o numero para ser multiplicado: '))

for cont in range(0, 11):
    total = num_escolhido * cont
    print('{} X {} = {}'.format(num_escolhido, cont, total))
print('TABUADA DO {}'.format(num_escolhido))
