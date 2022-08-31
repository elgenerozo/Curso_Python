"""Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:

- O primeiro valor é maior.
- O seundo valor é maior.
- Não exsite vamor maior, os dois são iguais."""

num1 = int(input('Entre com o primeiro numero: '))
num2 = int(input('Entre com o segundo numero: '))

if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1, num2))
elif num1 < num2:
    print('O número {} é menor que o número {}'.format(num1, num2))
else:
    print('Os números {} e {} são iguais'.format(num1, num2))

print('OBRIGADO!!!')
