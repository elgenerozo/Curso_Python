# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que
# a cada litro de tinhta, pinta uma área de 2 m ^ 2.


tinta_pinta = 2

larg = float(input('Entre com a largura da área a ser pintada: '))
alt = float(input('Entre com a altura da área a ser pintada: '))
total_area = larg*alt

print("Sua área quadrada é {:.2f} e você vai precisar de {:.2f}l de tinta".format(larg*alt, tinta_pinta*total_area))
