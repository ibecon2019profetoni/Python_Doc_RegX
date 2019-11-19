"""
    BUSCAR PATRONES
    ---------------
    Match = si hay coincidencias al INICIO de un string
    Search = busca en TODO el string
"""

import re

persona1 = 'Pedro Antonio'
persona2 = 'Julia Morrón'
persona3 = 'María Lucia'
persona4 = 'Cati Ripoll'
persona5 = 'Pati Fort'

codigo = 'skjdhf kjs19dhfjk shdjkfh djksfhjks72dhfjksdhfjk shdfjkhsdkhsdkjfh'
# MATCH ************************
if re.match('.ati', persona5):
    print('Encontrado')
else:
    print('NO Encontrado')

# --------------------------------
print('-' * 60)
#  match admite un tercer parámetro
if re.match('cati', persona4,re.IGNORECASE):
    print('Encontrado')
else:
    print('NO Encontrado')

# SEARCH *******************************
# --------------------------------
print('-' * 60)

if re.search('1972', codigo,re.IGNORECASE):
    print('Encontrado')
else:
    print('NO Encontrado')

# --------------------------------
print('-' * 60)
if re.search('antonio', persona1,re.IGNORECASE):
    print('Encontrado')
else:
    print('NO Encontrado')