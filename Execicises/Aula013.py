for cont in range(0, 10, 2):
    print(cont)
print('=*' * 50)
'''=================================================='''
for cont in range(10, 0, -2):
    print(cont)
print('=*' * 50)
'''=================================================='''
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM!')
print('=*' * 50)
'''=================================================='''
i = int(input('Início: '))
f = int(input('Fim: '))
salto = int(input('Salto:'))
for c in range(i, f, salto):
    print(c)
print('FIM!!!')
'''=================================================='''
for c1 in range(0, 3):
    n1 = int(input('Digite um valor: '))
print('FIM!!!!')
'''=================================================='''
s = 0
for c2 in range(0, 4):
    n2 = int(input('Digite um valor: '))
    s += n2
print('O somatório de todos os números foi {}'.format(s))
