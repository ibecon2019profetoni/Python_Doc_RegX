""" RANGOS """

import re

gente = [
    'Pedro',
    'Pepe',
    'María',
    'Cati',
    'María'
]

# Buscar en la lista a través de un rango
for nombre in gente:
    if re.findall('[a-c]', nombre):
        print(nombre)

# Buscar en la lista a través de un rango
for nombre in gente:
    if re.findall('^[A-C]', nombre):
        print(nombre)

# Buscar en la lista a través de un rango
for nombre in gente:
    if re.findall('[o-y]$', nombre):
        print(nombre)

# --------------------------------
print('-' * 60)

codigo_ventas = [
    'inf1',
    'dep1',
    'inf2',
    'hogar1',
    'inf3',
    'infA',
    'infB'
]

#  buscar en la lista rango de código de informática
for codigo in codigo_ventas:
    if re.findall('inf[0-9]', codigo):
        print(codigo)

print('-' * 60)
#  buscar en la lista rango que NIEGUE su condición
for codigo in codigo_ventas:
    if re.findall('inf[^0-2]', codigo):
        print(codigo)

print('-' * 60)
#  buscar en la lista varios rangos
for codigo in codigo_ventas:
    if re.findall('inf[0-9A-Za-z]', codigo):
        print(codigo)


