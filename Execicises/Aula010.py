
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro já esta ficando velhinho')
print('****FIM****')

# Outra maneira de ser feito (CONDIÇÃO SIMPLIFICADA)

print('Seu carro esta novo' if tempo <= 3 else 'Seu carro já esta fincando velhinho\n' '****FIM****')
