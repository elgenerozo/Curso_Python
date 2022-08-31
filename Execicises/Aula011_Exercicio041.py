"""Exercício 041 - A confederasção Nacional de Natação, pecisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo co a sua idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Acima: MASTER"""

import datetime

dt_nasc = int(input('Qual seu ano de nascimento: '))
data = datetime.date.today()
#   pegando o ano atual
#   atual = date.today().year

ano = int(data.strftime('%Y'))
diferenca_ano = (ano - dt_nasc)

if diferenca_ano <= 9:
    print('você tem {} anos e faz marte da categoria MIRIM'.format(diferenca_ano))
elif diferenca_ano > 9 and diferenca_ano < 13:
    print('Você tem {} anos e faz parte da equipe INFANTIL'.format(diferenca_ano))
elif diferenca_ano >= 14 and diferenca_ano <= 19:
    print('Você tem {} anos e faz parte da categoria JUNIOR'.format(diferenca_ano))
elif diferenca_ano > 19:
    print('Você tem {} anos e faz parte da categoria MASTER'.format(diferenca_ano))
