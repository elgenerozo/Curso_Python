nome = str(input('Qual é o seu nome? '))
if nome == 'Emerson':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil, {}!'.format(nome))
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino! {}'.format(nome))
else:
    print('Seu nome é bem normal, {}'.format(nome))
print('Tenha um bom dia, {}!'.format(nome))
