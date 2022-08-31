"""Exercícios 040 - Crie um programa que leia duas notas de um aluna e calcule a sua média, mostrando uma
mensagem no final, de acordo com a média atingida:

- Media abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

nota1 = float(input('Entre com sua primeira nota: '))
nota2 = float(input('Entre com sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Voce foi REPROVADO, estude mais e tente novamente')
elif media >= 5 and media <= 6.9:
    print('Você esta de recuperação, continue estudando')
elif media >= 7:
    print('Você foi aprovado, PARABÉNS!!!')
print('ATÉ O PROXIMO ANO!!!')

