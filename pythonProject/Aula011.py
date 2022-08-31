
nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Emerson':
    print('Que nome legal \033[4;31;36m{}\033[m!'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brail')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))
