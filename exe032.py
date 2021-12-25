# Ano bissexto

'''ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))'''

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))