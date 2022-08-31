"""Exercício 045 — Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
from time import sleep

print('JÔÔÔ')
sleep(3)
print('KEENNNN')
sleep(3)
print('PÔÔÔÔÔ')

lista = ['Pedra', 'Papel', 'Tesoura']
jogada_computador = randint(0, 2)

escolha = int(input('''Escolha suas opções: 
                    [0] - Pedra 
                    [1] - Papel 
                    [2] - Tesoura\n                       '''))

sleep(2)
print('=*' * 30)

print(f'Sua jogada foi {lista[escolha]}')
print(f'A jogada do computador foi {lista[jogada_computador]}')

if jogada_computador == 0 and escolha == 0:
    print('Empatou')
elif escolha == 1:
    print('Papel embrulha pedra!!! \n''VOCÊ VENCEU!!!!!')
elif escolha == 2:
    print('Pedra quebra tesoura! \n''O COMPUTADOR VENCEU, SE FODEU!!!')

elif jogada_computador == 1 and escolha == 0:
    print('Papel embrulha a pedra!!!\n' 'O COMPUTADOR VENCEU!!! SE FODEU!!!1')
elif escolha == 1:
    print('EMPATE!!!')
elif escolha == 2:
    print('Tesoura corta papel!!!\n''VOCÊ VENCEU!!!')

elif jogada_computador == 2 and escolha == 0:
    print('Pedra quebra tesoura!!!\n''VOCÊ VENCEU !!!')
elif escolha == 1:
    print('Tesoura corta papel!!!\n''O COMPUTADOR VENCEU SEU LIXO!!')
elif escolha == 2:
    print('EMPATOU')

else:
    print('JOGADA INVALIDA ANIMAL!!!!')
