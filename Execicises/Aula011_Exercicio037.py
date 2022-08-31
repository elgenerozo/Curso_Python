"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:

- 1 para binário.
- 2 para oct
- 3 para hexadecimal"""

num = int(input('Entre com o numero inteiro para ser convertido: '))

convertido_bin = "{0:b}".format(num)
convertido_oct = "{0:o}".format(num)
convertido_hex = "{0:x}".format(num)

menu = {'1': convertido_bin,
        '2': convertido_oct,
        '3': convertido_hex}
opcao = int(input('Digite 1 - Binário, 2 - Octal, 3 - Hex: '))

if opcao == 1:
    print('Convertido para binário: {}{}{}'.format('\033[1;3;41m', convertido_bin, '\033[m'))
    print('Convertido para binário: {}'.format(bin(num)[2:]))
elif opcao == 2:
    print('Convertido para Octal: {}{}{}'.format('\033[1;3;41m', convertido_oct, '\033[m'))
    print('Convertido para Octal: {}}'.format(oct(num)[2:]))
elif opcao == 3:
    print('Convertido para Hex: {}{}{}'.format('\033[1;3;41m', convertido_hex, '\033[m'))
    print('Convertido para Hex: {}'.format(hex(num)[2:]))

print('OBRIGADO!')
