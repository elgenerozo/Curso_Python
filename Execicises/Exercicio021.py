"""Faça um programa que leia a frase pelo teclado e mostre:
1 - Quantas vezes aparece a letra "A".
2 - Em que posição ela aparece pela primeira vez.
3 - Em que posição ela aparece pela última vez."""

frase = str(input('Entre com a sua frase: ')).strip()
print('A Letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece preiramente na posição {}'.format(frase.find('A')+1))
print('A letra A aparece pela última vez na posição {}'.format(frase.rfind('A')))
