"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é hora de se alistar.
- Se já passou o tempo de alistamento.

O seu programa também devera mostrar o tempo que falta ou que passou do prazo de alistamento."""

import datetime

dt_nasc = int(input('Qual seu ano de nascimento: '))
data = datetime.date.today()
ano = int(data.strftime('%Y'))
diferenca_ano = (ano - dt_nasc)
if diferenca_ano <= 18 and diferenca_ano < 17:
    print('Ainda não é hora de se alistar')
    print('Ainda faltam {} anos para você se alistar'.format(diferenca_ano - 18))
elif diferenca_ano <= 18 or diferenca_ano == 17:
    print('Esse ano você devera se alistar')
elif diferenca_ano >= 18:
    print('Você não precisará mais se alistar.')
else:
    print('Até mais !!!')
