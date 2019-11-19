import re

frase = 'Hoy es lunes y me suenan las tripas de no poder comer paella. Me importa un pepino lo que diga Youssef.'

# SEARCH, texto a buscar, texto donde buscar
print(re.search('Hoy', frase))

palabra = 'es'

if re.search(palabra, frase) is not None:
    print('Texto encontrado')
else:
    print('Texto No encontrado')


buscar = re.search(palabra, frase)

# primera posición donde se encuentra la palabra
print(buscar.start())
# última posición donde se encuentra la palabra
print(buscar.end())
# posción en una tupla
print(buscar.span())

