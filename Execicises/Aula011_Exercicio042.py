"""Exercício 042 -Refaça o desafio 035 dos triângulos, acrescentando o recurdo de mostrar
que tipo de triângulo será formado:

- Equilátero: Todos os lados são iguais.
- Isósceles: Dois lados são iguais.
- Todos dos lados são diferentes."""

reta1 = float(input('Entre com a medida da reta1: '))
reta2 = float(input('Entre com a medida da reta2: '))
reta3 = float(input('Entre com a medida da reta3: '))

if reta1 == reta2 and reta1 == reta3:
    print('Esse triangulo possuí todos os lados iguais, logo é um triângulo  EQUILATERO')
elif reta1 == reta2 or reta1 == reta3 or reta2 == reta1 or reta2 == reta3 or reta3 == reta1 or reta3 == reta2:
    print('Esse triângulo possuí, pelo menos dois lados iguais, logo é um triângo ISÓSCELES')
else:
    print('Esse triângulo possuí todos os lados diferêntes, logo é um triângulo ESCALENO')
print('AGORA VOCÊ JÁ CONHECE TODOS OS TIPOS DE TRIÂNGULOS')
