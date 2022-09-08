"""
Exercício053 — Crei um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços e acentos.

Ex.: Apos a sopa.
     A sacada da casa.
     A torre da derrota.
     O lobo ama o bolo.
     Anotaram a data da maratona.
"""

frase = str(input('Digite uma frase: ')).strip().upper()
frase = str(frase.replace(' ', ''))
print(frase)
frase_invertida = str(frase.replace(' ', '')[::-1])
print(frase_invertida)

if frase == frase_invertida:
    print('Essa frase é um políndromo')
else:
    print('Essa frase não é um políndromo')

"""OUTRA MANEIRA DE SER FEITO"""
print('\n' * 3)

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo!')

