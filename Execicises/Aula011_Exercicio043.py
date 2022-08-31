"""O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em m),
 de acordo com a seguinte fórmula: IMC = peso / (altura x altura). O resultado
 de IMC é dado em kg/m2"""

"""Exercicio 043 - Desenvolva uma lógica que leia o peso e a altua de uma pessoal, calcule
seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso.
- Entre 18.5 e 25: Peso ideal.
- 25 até 30: Sobrepeso.
- 30 até 40: Obesidade.
- Acima de 40: Obesidade Mórbida."""

peso = float(input('Qual é o seu peso: '))
altura = float(input('Qual é a sua altura: '))
imc = (peso / (altura * altura))

if imc < 18.5:
    print('Voce esta abaixo do peso.')
elif 18.5 > imc <= 25:
    print('Você esta no peso ideal.')
elif 25 > imc <= 30:
    print('Você esta com sobre peso!')
elif 30 > imc <= 40:
    print('Você esta com obesidade!')
elif 40 > imc:
    print('Você esta com obesidade morbida!')
print('Nunca deixe de se cuidar!!!')
