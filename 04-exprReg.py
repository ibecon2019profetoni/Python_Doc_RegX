"""
    Metacaracteres
    --------------
    (carácter comodín)
"""

""" ANCLAS """

import re

gente = [
    'Pedro Antonio',
    'Pepe Gonzalez',
    'María de Santos',
    'Cati Ripoll',
    'María Fort'
]

# Buscar en la lista nombre
for nombre in gente:
    if re.findall('^María', nombre):
        print(nombre)

# ------------------------------------
print('-' * 60)

# Buscar en la lista nombre
for nombre in gente:
    if re.findall('Ripoll$', nombre):
        print(nombre)

# ------------------------------------
print('-' * 60)
# ------------------------------------
print('-' * 60)


lista = [
    'http://www.toniferra.com',
    'http://www.toniferra.es',
    'http://www.tonifeça.it',
    'http://www.toniferra.fr',
    'https://www.toniferra.com',
]

#  Buscar en la lista la url más segura
for url in lista:
    if re.findall('^https', url):
        print(url)

print('-' * 60)      
#  Buscar en la lista la url de un país
for url in lista:
    if re.findall('fr$', url):
        print(url)

print('-' * 60)
# ----------------- RANGOS ------------------
for url in lista:
    if re.findall('[ç]', url):
        print(url)

for url in lista:
    if re.findall('[áÁ]', url):
        print(url)