print('\033[31mOlá mundo!!')
print('\033[31;43mOlá mundo!!')
print('\033[1;31;43mOlá mundo!!!\033[m')
print('\033[7;33;44mOlá mundo!!!\033[m')

a = 3
b = 5

print('Os valores são \033[0;34;33m{}\033[m e \033[31m{}\033[m'.format(a, b))
nome = 'Emerson'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\33[33m',
         'pretoebranco': '\033[7;30m'}

print('Olá, Meu nome é {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))

n ='Jose'
i = 25
print('{}{}')
