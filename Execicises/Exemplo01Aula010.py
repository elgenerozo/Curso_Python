n1 = float(input('Qual é a sua primeria nota: '))
n2 = float(input('Qual é a sua segunda nota: '))

media = (n1 + n2) / 2

print('Sua média é {}'.format(media))

if media >= 6:
    print('Sua média é boa, parabéns!')
else:
    print('Sua média esta baixa! ESTUDE MAIS DA PRÓXIMA VEZ')

# Outra maneira de se fazer (CONDIÇÃO SIMPLIFICADA)

print('PARABÉNS' if media >= 6 else 'ESTUDE MAIS DA PRÓXIMA VEZ!')
