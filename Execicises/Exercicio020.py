"""Crie um programa que leia o nome de uma pessoa, e diga se ela tem "Silva" no nome."""

nome = str(input('Entre como seu nome completo: ')).strip()

print('Você possui Silva no nome: {}'.format('SILVA' in nome.upper()))

