# ex.004 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
# informações possíveis sobre ele.


dado = input('Entre com o dado a ser analisado: ').split()
print(' O dado digitado foi: {} \n'.format(dado), 'E seu tipo primitivo é: {}'.format(type(dado)))
